"""Local filesystem storage backend."""

from __future__ import annotations

from pathlib import Path

from packages.config.settings import get_settings


class LocalStorage:
    def __init__(self, root: str | Path | None = None) -> None:
        settings = get_settings()
        self.root = Path(root or settings.storage_root)
        self.root.mkdir(parents=True, exist_ok=True)

    def job_dir(self, job_id: str) -> Path:
        path = self.root / job_id
        path.mkdir(parents=True, exist_ok=True)
        return path

    def path_for(self, job_id: str, filename: str) -> Path:
        return self.job_dir(job_id) / filename

    def public_url(self, job_id: str, filename: str) -> str:
        return f"/files/{job_id}/{filename}"

    def delete_job(self, job_id: str) -> None:
        path = self.root / job_id
        if path.exists():
            for child in path.iterdir():
                child.unlink(missing_ok=True)
            path.rmdir()
