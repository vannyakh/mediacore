"""Imgur provider — public oEmbed metadata; direct ``i.imgur.com`` media download."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

from packages.core.downloader import download_file, head_content_type
from packages.core.exceptions import FormatNotFoundError, ProviderNotConfiguredError
from packages.core.models import (
    DownloadResult,
    FormatInfo,
    Manifest,
    MediaMetadata,
    ProviderCapabilities,
    ThumbnailInfo,
)
from packages.core.parser import extension_from_url, hostname
from packages.core.provider import Provider
from providers.oembed import fetch_oembed, metadata_from_oembed

OEMBED_ENDPOINT = "https://api.imgur.com/oembed"


class ImgurProvider(Provider):
    name = "imgur"
    status = "active"
    capabilities = ProviderCapabilities(
        metadata=True,
        manifest=True,
        formats=True,
        download=True,
        thumbnail=True,
        subtitle=False,
        live=False,
    )

    def supports(self, url: str) -> bool:
        host = hostname(url)
        return host in {"imgur.com", "i.imgur.com", "www.imgur.com"} or host.endswith(".imgur.com")

    def _is_direct_media(self, url: str) -> bool:
        host = hostname(url)
        if host != "i.imgur.com" and not host.endswith(".imgur.com"):
            return False
        path = urlparse(url).path.lower()
        return any(
            path.endswith(ext)
            for ext in (".mp4", ".webm", ".gif", ".gifv", ".jpg", ".jpeg", ".png", ".webp")
        )

    def _direct_url(self, url: str) -> str:
        # .gifv is an HTML shell; Imgur serves the mp4 at the same stem
        if urlparse(url).path.lower().endswith(".gifv"):
            return url[:-5] + ".mp4"
        return url

    def metadata(self, url: str) -> MediaMetadata:
        if self._is_direct_media(url):
            media_url = self._direct_url(url)
            ctype = head_content_type(media_url)
            ext = extension_from_url(media_url) or "mp4"
            fmt = FormatInfo(
                id="original",
                quality="original",
                container=ext.lstrip("."),
                mime_type=ctype,
                url=media_url,
            )
            return MediaMetadata(
                platform=self.name,
                url=url,
                title=Path(urlparse(media_url).path).name or "Imgur media",
                formats=[fmt],
                manifest=Manifest(
                    type="direct",
                    provider=self.name,
                    url=media_url,
                    format_ids=[fmt.id],
                ),
            )
        data = fetch_oembed(OEMBED_ENDPOINT, url, provider_name=self.name)
        meta = metadata_from_oembed(self.name, url, data, title_fallback="Imgur media")
        # Gallery/page oEmbed has no permitted media URL — keep formats for analyze only
        return meta

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        if not self._is_direct_media(url):
            raise ProviderNotConfiguredError(
                f"{self.name} (use a direct i.imgur.com media URL; "
                "gallery pages need authorized Imgur API)"
            )
        meta = self.metadata(url)
        chosen = next((f for f in meta.formats if f.id == format_id), None)
        if chosen is None and format_id in {"original", "best", "default"}:
            chosen = meta.formats[0] if meta.formats else None
        if chosen is None or not chosen.url:
            raise FormatNotFoundError(format_id)
        if not dest.suffix and chosen.container:
            dest = dest.with_suffix("." + chosen.container.lstrip("."))
        size, ctype = download_file(chosen.url, dest)
        return DownloadResult(
            path=dest,
            format_id=chosen.id,
            container=chosen.container or "bin",
            filesize=size,
            content_type=ctype or chosen.mime_type,
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)
