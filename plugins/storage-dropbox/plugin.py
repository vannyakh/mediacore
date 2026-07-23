"""Dropbox storage — optional OAuth backend."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.storage.cloud import not_configured

PLUGIN = {
    "name": "mediacore-plugin-storage-dropbox",
    "version": "0.1.0",
    "kind": "storage",
    "description": "Dropbox storage (optional — set STORAGE_BACKEND=dropbox)",
    "status": "stub",
    "capabilities": ["store", "delete", "list", "publish"],
}


def create(settings: Any, *, root: str | Path | None = None) -> Any:
    token = getattr(settings, "dropbox_access_token", None)
    if not token:
        raise not_configured("Dropbox", "Set DROPBOX_ACCESS_TOKEN.")
    raise not_configured(
        "Dropbox",
        "Token present but Dropbox client is not implemented yet.",
    )
