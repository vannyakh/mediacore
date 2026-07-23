"""Azure Blob storage — optional; install azure-storage-blob extra when enabling."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.storage.cloud import not_configured

PLUGIN = {
    "name": "mediacore-plugin-storage-azure",
    "version": "0.1.0",
    "kind": "storage",
    "description": "Azure Blob storage (optional — set STORAGE_BACKEND=azure)",
    "status": "stub",
    "capabilities": ["store", "delete", "signed_url", "publish"],
}


def create(settings: Any, *, root: str | Path | None = None) -> Any:
    conn = getattr(settings, "azure_storage_connection_string", None)
    container = getattr(settings, "azure_storage_container", None)
    if not conn or not container:
        raise not_configured(
            "Azure Blob",
            "Set AZURE_STORAGE_CONNECTION_STRING and AZURE_STORAGE_CONTAINER.",
        )
    raise not_configured(
        "Azure Blob",
        "Connection present but Azure client is not implemented yet "
        "(uv sync --extra storage-azure planned).",
    )
