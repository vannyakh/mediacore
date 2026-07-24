"""Azure Blob storage — optional; requires azure-storage-blob extra."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.core.exceptions import PluginError
from packages.storage.base import StorageBackend
from packages.storage.local import LocalStorage


def _blob_service(connection_string: str) -> Any:
    try:
        from azure.storage.blob import BlobServiceClient
    except ImportError as exc:  # pragma: no cover
        raise PluginError(
            "Azure Blob storage requires azure-storage-blob. "
            "Install with: uv sync --extra storage-azure"
        ) from exc
    return BlobServiceClient.from_connection_string(connection_string)


class AzureBlobStorage(StorageBackend):
    """Local staging + upload to Azure Blob container."""

    name = "azure"

    def __init__(
        self,
        *,
        connection_string: str,
        container: str,
        staging_root: str | Path | None = None,
        public_base_url: str | None = None,
        prefix: str = "mediacore/",
    ) -> None:
        if not connection_string or not container:
            raise PluginError(
                "Azure storage is not configured "
                "(AZURE_STORAGE_CONNECTION_STRING / AZURE_STORAGE_CONTAINER)"
            )
        self.container = container
        self.prefix = prefix.rstrip("/") + "/"
        self.public_base_url = (public_base_url or "").rstrip("/")
        self._local = LocalStorage(root=staging_root)
        self.root = self._local.root
        self._service = _blob_service(connection_string)
        self._client = self._service.get_container_client(container)

    def job_dir(self, job_id: str) -> Path:
        return self._local.job_dir(job_id)

    def path_for(self, job_id: str, filename: str) -> Path:
        return self._local.path_for(job_id, filename)

    def _blob_name(self, job_id: str, filename: str) -> str:
        return f"{self.prefix}{job_id}/{filename}"

    def public_url(self, job_id: str, filename: str) -> str:
        blob = self._blob_name(job_id, filename)
        if self.public_base_url:
            return f"{self.public_base_url}/{blob}"
        return self._client.get_blob_client(blob).url

    def publish(self, job_id: str, path: Path) -> str:
        blob = self._blob_name(job_id, path.name)
        with path.open("rb") as fh:
            self._client.upload_blob(name=blob, data=fh, overwrite=True)
        return self.public_url(job_id, path.name)

    def delete_job(self, job_id: str) -> None:
        prefix = f"{self.prefix}{job_id}/"
        for item in self._client.list_blobs(name_starts_with=prefix):
            self._client.delete_blob(item.name)
        self._local.delete_job(job_id)

    @property
    def requires_cloud(self) -> bool:
        return True
