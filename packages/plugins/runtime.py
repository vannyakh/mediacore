"""Plugin runtime — resolve capabilities through the plugin layer."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from packages.core.exceptions import PluginError
from packages.media.wrapper import ffmpeg_available
from packages.plugins.kinds import PluginKind
from packages.plugins.loader import PluginInfo, PluginLoader, get_plugin_loader
from packages.storage.base import StorageBackend
from packages.storage.factory import BACKEND_PLUGINS, normalize_backend, resolve_storage

logger = logging.getLogger("mediacore.plugins.runtime")

STORAGE_LOCAL = "mediacore-plugin-storage-local"
FFMPEG_PLUGIN = "mediacore-plugin-ffmpeg"


class _IdentityNormalizer:
    def enrich(self, metadata: Any) -> Any:
        return metadata

# Kinds that receive EventBus events via on_event
_EVENT_KINDS = (
    PluginKind.NOTIFICATIONS,
    PluginKind.WEBHOOKS,
    PluginKind.ANALYTICS,
)


class PluginRuntime:
    def __init__(self, loader: PluginLoader | None = None) -> None:
        self.loader = loader or get_plugin_loader()

    def require(self, name: str, *, allow_stub: bool = False) -> PluginInfo:
        info = self.loader.get(name)
        if info is None:
            raise PluginError(f"Plugin not found: {name}")
        if info.status == "error":
            raise PluginError(f"Plugin '{name}' failed to load: {info.description}")
        if info.status == "disabled":
            raise PluginError(f"Plugin '{name}' is disabled")
        if info.status == "stub" and not allow_stub:
            raise PluginError(f"Plugin '{name}' is a stub and is not ready")
        if info.status not in {"available", "stub"}:
            raise PluginError(f"Plugin '{name}' is not available (status={info.status})")
        return info

    def resolve_by_kind(
        self,
        kind: PluginKind | str,
        *,
        capability: str | None = None,
        prefer: str | None = None,
        allow_stub: bool = False,
    ) -> PluginInfo:
        kind_enum = kind if isinstance(kind, PluginKind) else PluginKind(kind)
        candidates = self.loader.by_kind(kind_enum)
        if prefer:
            preferred = next((p for p in candidates if p.name == prefer), None)
            if preferred is not None:
                candidates = [preferred] + [p for p in candidates if p.name != prefer]
        for info in candidates:
            if capability and capability not in info.capabilities:
                continue
            if info.status == "available" or (allow_stub and info.status == "stub"):
                return info
        label = f"{kind_enum.value}" + (f"/{capability}" if capability else "")
        raise PluginError(f"No enabled plugin for {label}")

    def create(self, name: str, settings: Any | None = None, **kwargs: Any) -> Any:
        """Call a plugin's ``create()`` factory after require()."""
        info = self.require(name)
        module = info.module or {}
        factory = module.get("create")
        if factory is None:
            raise PluginError(f"Plugin '{name}' has no create() factory")
        if settings is None:
            from packages.config.settings import get_settings

            settings = get_settings()
        return factory(settings, **kwargs)

    def get_storage(self, root: str | Path | None = None) -> StorageBackend:
        """
        Resolve storage for the active STORAGE_BACKEND.

        Default is local. Cloud plugins are never required for a local-only workflow.
        """
        from packages.config.settings import get_settings

        settings = get_settings()
        backend = normalize_backend(settings.storage_backend)
        plugin_name = BACKEND_PLUGINS.get(backend, STORAGE_LOCAL)
        if backend == "local":
            self.require(STORAGE_LOCAL)
        else:
            self.require(plugin_name, allow_stub=True)
        return resolve_storage(settings, root=root)

    def ensure_ffmpeg(self) -> PluginInfo:
        info = self.require(FFMPEG_PLUGIN)
        if not ffmpeg_available():
            raise PluginError(
                f"Plugin '{FFMPEG_PLUGIN}' is available but the ffmpeg binary is not installed"
            )
        return info

    def ffmpeg(self) -> Any:
        """Return FFmpegService from the ffmpeg plugin."""
        return self.create(FFMPEG_PLUGIN)

    def metadata_normalizer(self) -> Any:
        """Optional metadata enricher; identity when no metadata plugin is installed."""
        info = self.loader.get("mediacore-plugin-metadata")
        if info is None or info.status != "available" or not info.module:
            return _IdentityNormalizer()
        try:
            return self.create("mediacore-plugin-metadata")
        except PluginError:
            return _IdentityNormalizer()

    def dispatch_event(self, event: Any) -> None:
        """Invoke on_event for notification, webhook, and analytics plugins."""
        for kind in _EVENT_KINDS:
            for info in self.loader.by_kind(kind):
                if info.status not in {"available", "stub"}:
                    continue
                module = info.module
                if not module:
                    continue
                handler = module.get("on_event")
                if handler is None:
                    continue
                # Skip stub notification plugins that aren't configured
                if info.status == "stub" and kind != PluginKind.ANALYTICS:
                    continue
                try:
                    handler(event)
                except Exception:  # noqa: BLE001
                    logger.exception("Plugin %s on_event failed", info.name)


_runtime: PluginRuntime | None = None


def get_runtime() -> PluginRuntime:
    global _runtime
    if _runtime is None:
        _runtime = PluginRuntime()
    return _runtime


def reset_runtime() -> None:
    global _runtime
    _runtime = None


def get_storage(root: str | Path | None = None) -> StorageBackend:
    return get_runtime().get_storage(root=root)


def ensure_ffmpeg() -> PluginInfo:
    return get_runtime().ensure_ffmpeg()
