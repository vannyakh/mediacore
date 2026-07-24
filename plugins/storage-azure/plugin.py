"""Azure Blob storage — optional; install azure-storage-blob extra when enabling."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.storage.azure import AzureBlobStorage
from packages.storage.cloud import not_configured

PLUGIN = {
    "name": "mediacore-plugin-storage-azure",
    "version": "0.1.0",
    "kind": "storage",
    "description": "Azure Blob storage (optional — set STORAGE_BACKEND=azure)",
    "status": "available",
    "capabilities": ["store", "delete", "signed_url", "publish"],
}


def create(settings: Any, *, root: str | Path | None = None) -> AzureBlobStorage:
    conn = getattr(settings, "azure_storage_connection_string", None)
    container = getattr(settings, "azure_storage_container", None)
    if not conn or not container:
        raise not_configured(
            "Azure Blob",
            "Set AZURE_STORAGE_CONNECTION_STRING and AZURE_STORAGE_CONTAINER.",
        )
    return AzureBlobStorage(
        connection_string=conn,
        container=container,
        staging_root=root or getattr(settings, "storage_root", None),
        public_base_url=getattr(settings, "azure_public_base_url", None),
    )
