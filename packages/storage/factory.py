"""Resolve the active storage backend. Default is local (no cloud required)."""

from __future__ import annotations

from pathlib import Path

from packages.config.settings import MediaCoreSettings, get_settings
from packages.core.exceptions import PluginError
from packages.storage.base import StorageBackend
from packages.storage.local import LocalStorage

# Maps STORAGE_BACKEND → plugin name
BACKEND_PLUGINS: dict[str, str] = {
    "local": "mediacore-plugin-storage-local",
    "s3": "mediacore-plugin-storage-s3",
    "r2": "mediacore-plugin-storage-r2",
    "gdrive": "mediacore-plugin-storage-gdrive",
    "google_drive": "mediacore-plugin-storage-gdrive",
    "azure": "mediacore-plugin-storage-azure",
    "azure_blob": "mediacore-plugin-storage-azure",
    "dropbox": "mediacore-plugin-storage-dropbox",
    "onedrive": "mediacore-plugin-storage-onedrive",
    "ftp": "mediacore-plugin-storage-ftp",
    "webdav": "mediacore-plugin-storage-webdav",
}


def normalize_backend(value: str | None) -> str:
    backend = (value or "local").strip().lower().replace("-", "_")
    if backend == "google_drive":
        return "gdrive"
    if backend == "azure_blob":
        return "azure"
    return backend or "local"


def resolve_storage(
    settings: MediaCoreSettings | None = None,
    *,
    root: str | Path | None = None,
) -> StorageBackend:
    """Return LocalStorage by default; cloud backends only when selected + configured."""
    settings = settings or get_settings()
    backend = normalize_backend(settings.storage_backend)
    if backend == "local":
        return LocalStorage(root=root or settings.storage_root)

    plugin_name = BACKEND_PLUGINS.get(backend)
    if plugin_name is None:
        raise PluginError(
            f"Unknown STORAGE_BACKEND={backend!r}. "
            f"Supported: {', '.join(sorted(set(BACKEND_PLUGINS)))}"
        )

    from packages.plugins.loader import get_plugin_loader

    loader = get_plugin_loader()
    info = loader.get(plugin_name)
    if info is None:
        raise PluginError(f"Storage plugin not found: {plugin_name}")
    module = info.module or {}
    create = module.get("create")
    if create is None:
        raise PluginError(
            f"Storage plugin '{plugin_name}' has no create() factory. "
            "Use STORAGE_BACKEND=local for local-only workflows."
        )
    storage = create(settings, root=root)
    if not isinstance(storage, StorageBackend):
        raise PluginError(f"Plugin '{plugin_name}' create() must return a StorageBackend")
    return storage
