"""Storage backend contract — cloud plugins are optional."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class StorageBackend(ABC):
    """Persist job artifacts. Local staging paths are always available for FFmpeg."""

    name: str = "storage"

    @abstractmethod
    def job_dir(self, job_id: str) -> Path:
        """Local directory for job working files."""

    @abstractmethod
    def path_for(self, job_id: str, filename: str) -> Path:
        """Local path for a job artifact."""

    @abstractmethod
    def public_url(self, job_id: str, filename: str) -> str:
        """URL clients can use to fetch the artifact (local path or remote URL)."""

    @abstractmethod
    def delete_job(self, job_id: str) -> None:
        """Remove local staging and any remote objects for the job."""

    def publish(self, job_id: str, path: Path) -> str:
        """Upload/finalize after a local write. Default: local public URL only."""
        return self.public_url(job_id, path.name)

    @property
    def requires_cloud(self) -> bool:
        return False
