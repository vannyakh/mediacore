"""Vimeo provider using public oEmbed (metadata only; no access-control bypass)."""

from __future__ import annotations

from pathlib import Path

import httpx

from packages.core.exceptions import ProviderError, ProviderNotConfiguredError
from packages.core.models import DownloadResult, FormatInfo, MediaMetadata
from packages.core.parser import hostname
from packages.core.provider import Provider


class VimeoProvider(Provider):
    name = "vimeo"
    status = "metadata_only"

    def supports(self, url: str) -> bool:
        host = hostname(url)
        return host == "vimeo.com" or host.endswith(".vimeo.com") or host == "player.vimeo.com"

    def get_metadata(self, url: str) -> MediaMetadata:
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

        return MediaMetadata(
            platform=self.name,
            url=url,
            title=data.get("title") or "Vimeo video",
            duration=data.get("duration"),
            thumbnail=data.get("thumbnail_url"),
            description=data.get("description"),
            author=data.get("author_name"),
            formats=[
                FormatInfo(id="oembed", quality="preview", container="html"),
            ],
            manifest={"type": "oembed", "provider_url": data.get("provider_url")},
            extra={"html": data.get("html")},
        )

    def list_formats(self, url: str) -> list[FormatInfo]:
        return self.get_metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (download requires an authorized Vimeo API token / owned content)"
        )
