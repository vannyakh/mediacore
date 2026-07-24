"""Generic HTTP provider for direct media URLs you control / may fetch."""

from __future__ import annotations

from pathlib import Path

from packages.core.models import (
    DownloadResult,
    FormatInfo,
    MediaMetadata,
    ProviderCapabilities,
    ThumbnailInfo,
)
from packages.core.parser import is_direct_media_url
from packages.core.provider import Provider
from providers.direct_media import direct_download, direct_metadata


class GenericHTTPProvider(Provider):
    name = "generic"
    status = "active"
    capabilities = ProviderCapabilities(
        metadata=True,
        manifest=True,
        formats=True,
        download=True,
        thumbnail=False,
        subtitle=False,
        live=False,
    )

    def supports(self, url: str) -> bool:
        return url.startswith(("http://", "https://")) and is_direct_media_url(url)

    def metadata(self, url: str) -> MediaMetadata:
        return direct_metadata(self.name, url)

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        return direct_download(self.name, url, format_id, dest)

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        return None
