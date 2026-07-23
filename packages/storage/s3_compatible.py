"""S3-compatible object storage (AWS S3, Cloudflare R2). Optional boto3."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.core.exceptions import PluginError
from packages.storage.base import StorageBackend
from packages.storage.local import LocalStorage


def _boto3_client(
    *,
    endpoint_url: str | None,
    region: str,
    access_key: str,
    secret_key: str,
) -> Any:
    try:
        import boto3
        from botocore.config import Config
    except ImportError as exc:  # pragma: no cover
        raise PluginError(
            "S3/R2 storage requires boto3. Install with: uv sync --extra storage-s3"
        ) from exc
    return boto3.client(
        "s3",
        endpoint_url=endpoint_url or None,
        region_name=region or "auto",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version="s3v4"),
    )


class S3CompatibleStorage(StorageBackend):
    """Local staging + optional upload to an S3-compatible bucket."""

    name = "s3"

    def __init__(
        self,
        *,
        bucket: str,
        access_key: str,
        secret_key: str,
        region: str = "us-east-1",
        endpoint_url: str | None = None,
        public_base_url: str | None = None,
        prefix: str = "mediacore/",
        staging_root: str | Path | None = None,
        backend_name: str = "s3",
    ) -> None:
        if not bucket or not access_key or not secret_key:
            raise PluginError(f"{backend_name} storage is not configured (bucket/keys required)")
        self.name = backend_name
        self.bucket = bucket
        self.prefix = prefix.rstrip("/") + "/"
        self.public_base_url = (public_base_url or "").rstrip("/")
        self._local = LocalStorage(root=staging_root)
        self.root = self._local.root
        self._client = _boto3_client(
            endpoint_url=endpoint_url,
            region=region,
            access_key=access_key,
            secret_key=secret_key,
        )

    def job_dir(self, job_id: str) -> Path:
        return self._local.job_dir(job_id)

    def path_for(self, job_id: str, filename: str) -> Path:
        return self._local.path_for(job_id, filename)

    def _key(self, job_id: str, filename: str) -> str:
        return f"{self.prefix}{job_id}/{filename}"

    def public_url(self, job_id: str, filename: str) -> str:
        if self.public_base_url:
            return f"{self.public_base_url}/{self._key(job_id, filename)}"
        return self._client.generate_presigned_url(
            "get_object",
            Params={"Bucket": self.bucket, "Key": self._key(job_id, filename)},
            ExpiresIn=3600,
        )

    def publish(self, job_id: str, path: Path) -> str:
        key = self._key(job_id, path.name)
        self._client.upload_file(str(path), self.bucket, key)
        return self.public_url(job_id, path.name)

    def delete_job(self, job_id: str) -> None:
        prefix = f"{self.prefix}{job_id}/"
        listed = self._client.list_objects_v2(Bucket=self.bucket, Prefix=prefix)
        for obj in listed.get("Contents") or []:
            self._client.delete_object(Bucket=self.bucket, Key=obj["Key"])
        self._local.delete_job(job_id)

    @property
    def requires_cloud(self) -> bool:
        return True
