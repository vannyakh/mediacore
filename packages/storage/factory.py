"""Resolve the active storage backend. Slim install: local only."""

from __future__ import annotations

from pathlib import Path

from packages.config.settings import MediaCoreSettings, get_settings
from packages.core.exceptions import PluginError
from packages.storage.base import StorageBackend
from packages.storage.local import LocalStorage

BACKEND_PLUGINS: dict[str, str] = {
    "local": "mediacore-plugin-storage-local",
}


def normalize_backend(value: str | None) -> str:
    backend = (value or "local").strip().lower().replace("-", "_")
    return backend or "local"


def resolve_storage(
    settings: MediaCoreSettings | None = None,
    *,
    root: str | Path | None = None,
) -> StorageBackend:
    settings = settings or get_settings()
    backend = normalize_backend(settings.storage_backend)
    if backend == "local":
        return LocalStorage(root=root or settings.storage_root)

    raise PluginError(
        f"Unknown STORAGE_BACKEND={backend!r}. "
        "Slim MediaCore supports local only (STORAGE_BACKEND=local)."
    )
