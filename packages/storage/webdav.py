"""WebDAV storage backend (httpx). Optional remote; local staging always used."""

from __future__ import annotations

from pathlib import Path

import httpx

from packages.core.exceptions import PluginError
from packages.storage.base import StorageBackend
from packages.storage.local import LocalStorage


class WebDAVStorage(StorageBackend):
    name = "webdav"

    def __init__(
        self,
        *,
        base_url: str,
        username: str = "",
        password: str = "",
        staging_root: str | Path | None = None,
    ) -> None:
        if not base_url:
            raise PluginError("WebDAV storage is not configured (WEBDAV_URL required)")
        self.base_url = base_url.rstrip("/")
        self.auth = (username, password) if username else None
        self._local = LocalStorage(root=staging_root)
        self.root = self._local.root

    def _url(self, job_id: str, filename: str | None = None) -> str:
        if filename:
            return f"{self.base_url}/{job_id}/{filename}"
        return f"{self.base_url}/{job_id}"

    def job_dir(self, job_id: str) -> Path:
        return self._local.job_dir(job_id)

    def path_for(self, job_id: str, filename: str) -> Path:
        return self._local.path_for(job_id, filename)

    def public_url(self, job_id: str, filename: str) -> str:
        return self._url(job_id, filename)

    def publish(self, job_id: str, path: Path) -> str:
        dir_url = self._url(job_id)
        file_url = self._url(job_id, path.name)
        with httpx.Client(auth=self.auth, timeout=60.0) as client:
            client.request("MKCOL", dir_url)
            with path.open("rb") as fh:
                res = client.put(file_url, content=fh)
                res.raise_for_status()
        return file_url

    def delete_job(self, job_id: str) -> None:
        with httpx.Client(auth=self.auth, timeout=60.0) as client:
            # Best-effort recursive delete via Depth header (server-dependent)
            client.request("DELETE", self._url(job_id), headers={"Depth": "infinity"})
        self._local.delete_job(job_id)

    @property
    def requires_cloud(self) -> bool:
        return True
