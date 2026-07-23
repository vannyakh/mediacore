"""Amazon S3 storage plugin — optional; requires STORAGE_BACKEND=s3 + credentials."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.core.exceptions import PluginError
from packages.storage.s3_compatible import S3CompatibleStorage

PLUGIN = {
    "name": "mediacore-plugin-storage-s3",
    "version": "0.1.0",
    "kind": "storage",
    "description": "Amazon S3 object storage (optional — set STORAGE_BACKEND=s3)",
    "status": "available",
    "capabilities": ["store", "delete", "signed_url", "publish"],
}


def create(settings: Any, *, root: str | Path | None = None) -> S3CompatibleStorage:
    bucket = getattr(settings, "s3_bucket", None)
    access = getattr(settings, "s3_access_key", None)
    secret = getattr(settings, "s3_secret_key", None)
    if not bucket or not access or not secret:
        raise PluginError(
            "S3 storage not configured. Set S3_BUCKET, S3_ACCESS_KEY, S3_SECRET_KEY "
            "or keep STORAGE_BACKEND=local."
        )
    return S3CompatibleStorage(
        bucket=bucket,
        access_key=access,
        secret_key=secret,
        region=getattr(settings, "s3_region", "us-east-1") or "us-east-1",
        endpoint_url=getattr(settings, "s3_endpoint_url", None),
        public_base_url=getattr(settings, "s3_public_base_url", None),
        prefix=getattr(settings, "s3_prefix", "mediacore/") or "mediacore/",
        staging_root=root or getattr(settings, "storage_root", None),
        backend_name="s3",
    )
