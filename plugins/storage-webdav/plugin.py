"""WebDAV storage plugin — optional; uses httpx when configured."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.core.exceptions import PluginError
from packages.storage.webdav import WebDAVStorage

PLUGIN = {
    "name": "mediacore-plugin-storage-webdav",
    "version": "0.1.0",
    "kind": "storage",
    "description": "WebDAV storage (optional — set STORAGE_BACKEND=webdav)",
    "status": "available",
    "capabilities": ["store", "delete", "public_url", "publish"],
}


def create(settings: Any, *, root: str | Path | None = None) -> WebDAVStorage:
    url = getattr(settings, "webdav_url", None)
    if not url:
        raise PluginError(
            "WebDAV storage not configured. Set WEBDAV_URL or keep STORAGE_BACKEND=local."
        )
    return WebDAVStorage(
        base_url=url,
        username=getattr(settings, "webdav_username", "") or "",
        password=getattr(settings, "webdav_password", "") or "",
        staging_root=root or getattr(settings, "storage_root", None),
    )
