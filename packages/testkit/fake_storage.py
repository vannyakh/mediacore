"""In-memory / temp-dir storage backend matching StorageBackend API."""

from __future__ import annotations

from pathlib import Path

from packages.storage.base import StorageBackend


class FakeStorage(StorageBackend):
    name = "fake"

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.deleted: list[str] = []
        self.published: list[tuple[str, str]] = []

    def job_dir(self, job_id: str) -> Path:
        path = self.root / job_id
        path.mkdir(parents=True, exist_ok=True)
        return path

    def path_for(self, job_id: str, filename: str) -> Path:
        return self.job_dir(job_id) / filename

    def public_url(self, job_id: str, filename: str) -> str:
        return f"/files/{job_id}/{filename}"

    def publish(self, job_id: str, path: Path) -> str:
        self.published.append((job_id, path.name))
        return self.public_url(job_id, path.name)

    def delete_job(self, job_id: str) -> None:
        path = self.root / job_id
        self.deleted.append(job_id)
        if path.exists():
            for child in path.iterdir():
                child.unlink(missing_ok=True)
            path.rmdir()
