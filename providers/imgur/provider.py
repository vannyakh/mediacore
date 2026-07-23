"""Imgur provider using public oEmbed (metadata only)."""

from __future__ import annotations

from pathlib import Path

from packages.core.exceptions import ProviderNotConfiguredError
from packages.core.models import (
    DownloadResult,
    FormatInfo,
    MediaMetadata,
    ProviderCapabilities,
    ThumbnailInfo,
)
from packages.core.parser import hostname
from packages.core.provider import Provider
from providers.oembed import fetch_oembed, metadata_from_oembed

OEMBED_ENDPOINT = "https://api.imgur.com/oembed"


class ImgurProvider(Provider):
    name = "imgur"
    status = "metadata_only"
    capabilities = ProviderCapabilities(
        metadata=True,
        manifest=True,
        formats=True,
        download=False,
        thumbnail=True,
        subtitle=False,
        live=False,
    )

    def supports(self, url: str) -> bool:
        host = hostname(url)
        return host in {"imgur.com", "i.imgur.com", "www.imgur.com"} or host.endswith(".imgur.com")

    def metadata(self, url: str) -> MediaMetadata:
        data = fetch_oembed(OEMBED_ENDPOINT, url, provider_name=self.name)
        return metadata_from_oembed(self.name, url, data, title_fallback="Imgur media")

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (download requires authorized Imgur API access)"
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)
