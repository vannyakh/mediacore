"""Google Drive storage — optional OAuth backend (stub until credentials wired)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.storage.cloud import not_configured

PLUGIN = {
    "name": "mediacore-plugin-storage-gdrive",
    "version": "0.1.0",
    "kind": "storage",
    "description": "Google Drive storage (optional — OAuth; not required for local use)",
    "status": "stub",
    "capabilities": ["store", "delete", "list", "publish"],
}


def create(settings: Any, *, root: str | Path | None = None) -> Any:
    creds = getattr(settings, "gdrive_credentials_json", None)
    if not creds:
        raise not_configured(
            "Google Drive",
            "Set GDRIVE_CREDENTIALS_JSON and GDRIVE_FOLDER_ID.",
        )
    raise not_configured(
        "Google Drive",
        "Credentials present but Drive client is not implemented yet.",
    )
