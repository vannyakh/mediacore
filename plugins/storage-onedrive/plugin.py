"""OneDrive storage — optional Microsoft Graph backend."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.storage.cloud import not_configured

PLUGIN = {
    "name": "mediacore-plugin-storage-onedrive",
    "version": "0.1.0",
    "kind": "storage",
    "description": "OneDrive storage (optional — set STORAGE_BACKEND=onedrive)",
    "status": "stub",
    "capabilities": ["store", "delete", "list", "publish"],
}


def create(settings: Any, *, root: str | Path | None = None) -> Any:
    token = getattr(settings, "onedrive_access_token", None)
    if not token:
        raise not_configured("OneDrive", "Set ONEDRIVE_ACCESS_TOKEN.")
    raise not_configured(
        "OneDrive",
        "Token present but OneDrive client is not implemented yet.",
    )
