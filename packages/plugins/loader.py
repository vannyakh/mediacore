"""Plugin loader — MediaCore stays small; capabilities come from plugins."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from packages.plugins.kinds import (
    DEFAULT_CAPABILITIES,
    PLUGIN_STATUSES,
    PluginKind,
    parse_plugin_kind,
)

logger = logging.getLogger("mediacore.plugins")


@dataclass
class PluginInfo:
    name: str
    version: str = "0.1.0"
    kind: str = PluginKind.STORAGE.value
    description: str = ""
    status: str = "available"
    path: str | None = None
    capabilities: list[str] = field(default_factory=list)
    module: dict[str, Any] | None = field(default=None, repr=False)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "version": self.version,
            "kind": self.kind,
            "description": self.description,
            "status": self.status,
            "path": self.path,
            "capabilities": self.capabilities,
        }


class PluginLoader:
    """Discovers plugin manifests under ./plugins/*/plugin.py."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or Path(__file__).resolve().parents[2] / "plugins"
        self._plugins: dict[str, PluginInfo] = {}

    def discover(self) -> list[PluginInfo]:
        self._plugins.clear()
        if not self.root.exists():
            return []
        for entry in sorted(self.root.iterdir()):
            if not entry.is_dir():
                continue
            manifest = entry / "plugin.py"
            if not manifest.exists():
                # Placeholder directory without implementation
                kind_guess = entry.name.split("-")[0] if "-" in entry.name else entry.name
                try:
                    kind = parse_plugin_kind(kind_guess).value
                except ValueError:
                    kind = kind_guess
                info = PluginInfo(
                    name=f"mediacore-plugin-{entry.name}",
                    kind=kind,
                    description=f"Scaffold for {entry.name}",
                    status="stub",
                    path=str(entry),
                )
                self._plugins[info.name] = info
                continue
            try:
                info = self._load_manifest(entry)
                self._plugins[info.name] = info
            except Exception as exc:  # noqa: BLE001
                logger.warning("Failed to load plugin %s: %s", entry.name, exc)
                info = PluginInfo(
                    name=f"mediacore-plugin-{entry.name}",
                    status="error",
                    description=str(exc),
                    path=str(entry),
                )
                self._plugins[info.name] = info
        return list(self._plugins.values())

    def _load_manifest(self, entry: Path) -> PluginInfo:
        ns: dict[str, Any] = {}
        code = (entry / "plugin.py").read_text(encoding="utf-8")
        exec(compile(code, str(entry / "plugin.py"), "exec"), ns, ns)  # noqa: S102
        meta = ns.get("PLUGIN") or ns.get("plugin") or {}
        if hasattr(meta, "to_dict") and not isinstance(meta, dict):
            info = meta
            if isinstance(info, PluginInfo):
                info.module = ns
            return info
        kind_raw = meta.get("kind", "storage")
        try:
            kind = parse_plugin_kind(str(kind_raw)).value
        except ValueError:
            raise ValueError(f"Unknown plugin kind: {kind_raw}") from None
        status = meta.get("status", "available")
        if status not in PLUGIN_STATUSES:
            raise ValueError(f"Invalid plugin status: {status}")
        caps = list(meta.get("capabilities") or [])
        if not caps:
            kind_enum = PluginKind(kind)
            caps = list(DEFAULT_CAPABILITIES.get(kind_enum, []))
        return PluginInfo(
            name=meta.get("name", f"mediacore-plugin-{entry.name}"),
            version=meta.get("version", "0.1.0"),
            kind=kind,
            description=meta.get("description", ""),
            status=status,
            path=str(entry),
            capabilities=caps,
            module=ns,
        )

    def list(self) -> list[PluginInfo]:
        if not self._plugins:
            self.discover()
        return list(self._plugins.values())

    def get(self, name: str) -> PluginInfo | None:
        if not self._plugins:
            self.discover()
        return self._plugins.get(name)

    def by_kind(self, kind: PluginKind | str) -> list[PluginInfo]:
        kind_value = kind.value if isinstance(kind, PluginKind) else parse_plugin_kind(kind).value
        return [p for p in self.list() if p.kind == kind_value]

    def enabled(self) -> list[PluginInfo]:
        return [p for p in self.list() if p.status in {"available", "stub"}]


_loader: PluginLoader | None = None


def get_plugin_loader() -> PluginLoader:
    global _loader
    if _loader is None:
        _loader = PluginLoader()
        _loader.discover()
    return _loader


def reset_plugin_loader() -> None:
    """Clear the process-wide loader (tests)."""
    global _loader
    _loader = None
