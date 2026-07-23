"""Generic HTTP provider for direct media URLs you control / may fetch."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlparse

from packages.core.downloader import download_file, head_content_type
from packages.core.exceptions import FormatNotFoundError, ProviderError
from packages.core.models import (
    DownloadResult,
    FormatInfo,
    Manifest,
    MediaMetadata,
    ProviderCapabilities,
    ThumbnailInfo,
)
from packages.core.parser import is_direct_media_url
from packages.core.provider import Provider


def _extension_from_url(url: str, default: str = "mp4") -> str:
    path = urlparse(url).path
    if "." in path.rsplit("/", 1)[-1]:
        return path.rsplit(".", 1)[-1].lower()
    return default


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
        filename = unquote(urlparse(url).path.rsplit("/", 1)[-1] or "media")
        content_type = head_content_type(url)
        ext = _extension_from_url(url)
        fmt = FormatInfo(
            id="original",
            quality="original",
            container=ext,
            mime_type=content_type,
            url=url,
        )
        manifest = Manifest(
            type="direct",
            provider=self.name,
            url=url,
            format_ids=[fmt.id],
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=filename,
            formats=[fmt],
            manifest=manifest,
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        meta = self.metadata(url)
        fmt = next((f for f in meta.formats if f.id == format_id or f.quality == format_id), None)
        if fmt is None:
            raise FormatNotFoundError(format_id)
        if not fmt.url:
            raise ProviderError(self.name, "No downloadable URL for format")
        target = dest if dest.suffix else dest.with_suffix(f".{fmt.container}")
        size, content_type = download_file(fmt.url, target)
        return DownloadResult(
            path=target,
            format_id=fmt.id,
            container=fmt.container,
            filesize=size,
            content_type=content_type or fmt.mime_type,
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        return None
