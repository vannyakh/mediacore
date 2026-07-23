"""Cloudflare R2 storage plugin — optional S3-compatible backend."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.core.exceptions import PluginError
from packages.storage.s3_compatible import S3CompatibleStorage

PLUGIN = {
    "name": "mediacore-plugin-storage-r2",
    "version": "0.1.0",
    "kind": "storage",
    "description": "Cloudflare R2 object storage (optional — set STORAGE_BACKEND=r2)",
    "status": "available",
    "capabilities": ["store", "delete", "signed_url", "publish"],
}


def create(settings: Any, *, root: str | Path | None = None) -> S3CompatibleStorage:
    account = getattr(settings, "r2_account_id", None)
    bucket = getattr(settings, "r2_bucket", None)
    access = getattr(settings, "r2_access_key", None)
    secret = getattr(settings, "r2_secret_key", None)
    if not account or not bucket or not access or not secret:
        raise PluginError(
            "R2 storage not configured. Set R2_ACCOUNT_ID, R2_BUCKET, R2_ACCESS_KEY, "
            "R2_SECRET_KEY or keep STORAGE_BACKEND=local."
        )
    endpoint = f"https://{account}.r2.cloudflarestorage.com"
    return S3CompatibleStorage(
        bucket=bucket,
        access_key=access,
        secret_key=secret,
        region="auto",
        endpoint_url=endpoint,
        public_base_url=getattr(settings, "r2_public_base_url", None),
        prefix=getattr(settings, "s3_prefix", "mediacore/") or "mediacore/",
        staging_root=root or getattr(settings, "storage_root", None),
        backend_name="r2",
    )
