"""Example provider demonstrating the full MediaCore provider surface."""

from __future__ import annotations

from pathlib import Path

from packages.core.exceptions import ProviderNotConfiguredError
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
from packages.core.provider import Provider


class ExampleProvider(Provider):
    name = "example"
    status = "example"
    capabilities = ProviderCapabilities(
        metadata=True,
        manifest=True,
        formats=True,
        download=False,
        thumbnail=True,
        subtitle=True,
        live=True,
    )

    def supports(self, url: str) -> bool:
        return url.startswith("mediacore://example/")

    def metadata(self, url: str) -> MediaMetadata:
        is_live = url.rstrip("/").endswith("/live")
        fmt = FormatInfo(id="demo", quality="720p", container="mp4")
        return MediaMetadata(
            platform=self.name,
            url=url,
            title="Example Media",
            duration=None if is_live else 12.0,
            thumbnail="https://example.com/thumb.jpg",
            formats=[fmt],
            manifest=Manifest(
                type="example",
                provider=self.name,
                url=url,
                format_ids=[fmt.id],
                is_live=is_live,
            ),
            is_live=is_live,
            subtitles=[
                SubtitleTrack(id="en", language="en", label="English", format="vtt"),
            ],
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (demo provider — no real media payload)"
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        meta = self.metadata(url)
        return ThumbnailInfo(url=meta.thumbnail) if meta.thumbnail else None

    def subtitles(self, url: str) -> list[SubtitleTrack]:
        return self.metadata(url).subtitles

    def live(self, url: str) -> LiveInfo | None:
        meta = self.metadata(url)
        if meta.is_live:
            return LiveInfo(is_live=True, status="live", stream_url=url)
        return LiveInfo(is_live=False, status="ended")
