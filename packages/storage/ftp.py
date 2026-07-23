"""FTP storage backend (stdlib ftplib). Optional remote; local staging always used."""

from __future__ import annotations

from ftplib import FTP, error_perm
from pathlib import Path

from packages.core.exceptions import PluginError
from packages.storage.base import StorageBackend
from packages.storage.local import LocalStorage


class FTPStorage(StorageBackend):
    name = "ftp"

    def __init__(
        self,
        *,
        host: str,
        username: str,
        password: str,
        port: int = 21,
        remote_root: str = "/mediacore",
        staging_root: str | Path | None = None,
        public_base_url: str | None = None,
    ) -> None:
        if not host:
            raise PluginError("FTP storage is not configured (FTP_HOST required)")
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.remote_root = remote_root.rstrip("/") or "/mediacore"
        self.public_base_url = (public_base_url or "").rstrip("/")
        self._local = LocalStorage(root=staging_root)
        self.root = self._local.root

    def _connect(self) -> FTP:
        ftp = FTP()
        ftp.connect(self.host, self.port, timeout=30)
        ftp.login(self.username, self.password)
        return ftp

    def _ensure_dirs(self, ftp: FTP, remote_dir: str) -> None:
        parts = [p for p in remote_dir.split("/") if p]
        path = ""
        for part in parts:
            path += f"/{part}"
            try:
                ftp.mkd(path)
            except error_perm:
                pass

    def job_dir(self, job_id: str) -> Path:
        return self._local.job_dir(job_id)

    def path_for(self, job_id: str, filename: str) -> Path:
        return self._local.path_for(job_id, filename)

    def public_url(self, job_id: str, filename: str) -> str:
        if self.public_base_url:
            return f"{self.public_base_url}/{job_id}/{filename}"
        return f"ftp://{self.host}{self.remote_root}/{job_id}/{filename}"

    def publish(self, job_id: str, path: Path) -> str:
        remote_dir = f"{self.remote_root}/{job_id}"
        with self._connect() as ftp:
            self._ensure_dirs(ftp, remote_dir)
            with path.open("rb") as fh:
                ftp.storbinary(f"STOR {remote_dir}/{path.name}", fh)
        return self.public_url(job_id, path.name)

    def delete_job(self, job_id: str) -> None:
        remote_dir = f"{self.remote_root}/{job_id}"
        try:
            with self._connect() as ftp:
                try:
                    names = ftp.nlst(remote_dir)
                except error_perm:
                    names = []
                for name in names:
                    base = name.rsplit("/", 1)[-1]
                    if base in {".", ".."}:
                        continue
                    try:
                        ftp.delete(f"{remote_dir}/{base}")
                    except error_perm:
                        pass
                try:
                    ftp.rmd(remote_dir)
                except error_perm:
                    pass
        except OSError:
            pass
        self._local.delete_job(job_id)

    @property
    def requires_cloud(self) -> bool:
        return True
