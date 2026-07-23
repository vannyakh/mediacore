"""Provider interface — Metadata, Manifest, Formats, Download, Thumbnail, Subtitle, Live."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from packages.core.exceptions import NotImplementedStageError
from packages.core.models import (
    DownloadResult,
    FormatInfo,
    LiveInfo,
    Manifest,
    MediaMetadata,
    ProviderCapabilities,
    SubtitleTrack,
    ThumbnailInfo,
)


class Provider(ABC):
    """Common interface for every media source provider.

    Architecture::

        Provider
        ├── Metadata
        ├── Manifest
        ├── Formats
        ├── Download
        ├── Thumbnail
        ├── Subtitle
        └── Live
    """

    name: str
    status: str = "active"
    capabilities: ProviderCapabilities = ProviderCapabilities()

    @abstractmethod
    def supports(self, url: str) -> bool: ...

    # --- Metadata ---
    @abstractmethod
    def metadata(self, url: str) -> MediaMetadata: ...

    # --- Manifest ---
    def manifest(self, url: str) -> Manifest:
        meta = self.metadata(url)
        if isinstance(meta.manifest, Manifest):
            return meta.manifest
        if isinstance(meta.manifest, dict):
            data = meta.manifest
            return Manifest(
                type=str(data.get("type") or "unknown"),
                provider=meta.platform,
                url=data.get("url") or meta.url,
                format_ids=list(data.get("format_ids") or [f.id for f in meta.formats]),
                is_live=bool(data.get("is_live") or meta.is_live),
                extra={k: v for k, v in data.items() if k not in {"type", "url", "format_ids", "is_live"}},
            )
        return Manifest(
            type="basic",
            provider=meta.platform,
            url=meta.url,
            format_ids=[f.id for f in meta.formats],
            is_live=meta.is_live,
        )

    # --- Formats ---
    def formats(self, url: str) -> list[FormatInfo]:
        meta = self.metadata(url)
        if meta.formats:
            return meta.formats
        raise NotImplementedStageError("formats")

    # --- Download ---
    @abstractmethod
    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult: ...

    # --- Thumbnail ---
    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        if not self.capabilities.thumbnail:
            return None
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)

    # --- Subtitle ---
    def subtitles(self, url: str) -> list[SubtitleTrack]:
        if not self.capabilities.subtitle:
            return []
        meta = self.metadata(url)
        return list(meta.subtitles)

    # --- Live ---
    def live(self, url: str) -> LiveInfo | None:
        if not self.capabilities.live:
            return None
        meta = self.metadata(url)
        if not meta.is_live:
            return LiveInfo(is_live=False, status="ended")
        return LiveInfo(is_live=True, status="live", stream_url=meta.url)

    # --- Back-compat aliases ---
    def get_metadata(self, url: str) -> MediaMetadata:
        return self.metadata(url)

    def list_formats(self, url: str) -> list[FormatInfo]:
        return self.formats(url)

    def capability_list(self) -> list[str]:
        return self.capabilities.to_list()
