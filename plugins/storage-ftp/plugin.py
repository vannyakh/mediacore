"""FTP storage plugin — optional; uses stdlib ftplib when configured."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.core.exceptions import PluginError
from packages.storage.ftp import FTPStorage

PLUGIN = {
    "name": "mediacore-plugin-storage-ftp",
    "version": "0.1.0",
    "kind": "storage",
    "description": "FTP storage (optional — set STORAGE_BACKEND=ftp)",
    "status": "available",
    "capabilities": ["store", "delete", "public_url", "publish"],
}


def create(settings: Any, *, root: str | Path | None = None) -> FTPStorage:
    host = getattr(settings, "ftp_host", None)
    if not host:
        raise PluginError("FTP storage not configured. Set FTP_HOST or keep STORAGE_BACKEND=local.")
    return FTPStorage(
        host=host,
        username=getattr(settings, "ftp_username", "anonymous") or "anonymous",
        password=getattr(settings, "ftp_password", "") or "",
        port=int(getattr(settings, "ftp_port", 21) or 21),
        remote_root=getattr(settings, "ftp_remote_root", "/mediacore") or "/mediacore",
        staging_root=root or getattr(settings, "storage_root", None),
        public_base_url=getattr(settings, "ftp_public_base_url", None),
    )
