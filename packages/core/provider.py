"""Provider interface — core must not depend on specific providers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from packages.core.models import DownloadResult, FormatInfo, MediaMetadata


class Provider(ABC):
    """Common interface for every media source provider."""

    name: str
    status: str = "active"

    @abstractmethod
    def supports(self, url: str) -> bool: ...

    @abstractmethod
    def get_metadata(self, url: str) -> MediaMetadata: ...

    @abstractmethod
    def list_formats(self, url: str) -> list[FormatInfo]: ...

    @abstractmethod
    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult: ...

    def thumbnail(self, url: str) -> str | None:
        return self.get_metadata(url).thumbnail

    def subtitles(self, url: str) -> list[dict]:
        return []
