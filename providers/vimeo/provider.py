"""Vimeo provider using public oEmbed (metadata/thumbnail; download not configured)."""

from __future__ import annotations

from pathlib import Path

import httpx

from packages.core.exceptions import ProviderError, ProviderNotConfiguredError
from packages.core.models import (
    DownloadResult,
    FormatInfo,
    Manifest,
    MediaMetadata,
    ProviderCapabilities,
    ThumbnailInfo,
)
from packages.core.parser import hostname
from packages.core.provider import Provider


class VimeoProvider(Provider):
    name = "vimeo"
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
        return host == "vimeo.com" or host.endswith(".vimeo.com") or host == "player.vimeo.com"

    def metadata(self, url: str) -> MediaMetadata:
        try:
            with httpx.Client(timeout=30.0, follow_redirects=True) as client:
                response = client.get(
                    "https://vimeo.com/api/oembed.json",
                    params={"url": url},
                    headers={"User-Agent": "MediaCore/0.1"},
                )
                if response.status_code == 404:
                    raise ProviderError(self.name, "Video not found or not publicly embeddable")
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPError as exc:
            raise ProviderError(self.name, f"oEmbed request failed: {exc}") from exc

        fmt = FormatInfo(id="oembed", quality="preview", container="html")
        manifest = Manifest(
            type="oembed",
            provider=self.name,
            url=url,
            format_ids=[fmt.id],
            extra={"provider_url": data.get("provider_url")},
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=data.get("title") or "Vimeo video",
            duration=data.get("duration"),
            thumbnail=data.get("thumbnail_url"),
            description=data.get("description"),
            author=data.get("author_name"),
            formats=[fmt],
            manifest=manifest,
            extra={"html": data.get("html")},
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (download requires an authorized Vimeo API token / owned content)"
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)
