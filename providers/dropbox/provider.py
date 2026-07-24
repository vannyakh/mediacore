"""Dropbox provider — shared file links via official ``dl=1`` (Help: force download)."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import parse_qs, unquote, urlencode, urlparse, urlunparse

from packages.core.downloader import download_file, head_content_type
from packages.core.exceptions import FormatNotFoundError, ProviderError, ProviderNotConfiguredError
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

# Share file paths Dropbox documents for dl=1 / raw=1 (not folder /sh/ shares).
_FILE_PREFIXES = ("/s/", "/scl/fi/", "/s/raw/", "/s/dl/")


def force_download_url(url: str) -> str:
    """Set Dropbox's documented ``dl=1`` query param on shared links."""
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    if host.endswith("dropboxusercontent.com"):
        return url
    qs = parse_qs(parsed.query, keep_blank_values=True)
    qs["dl"] = ["1"]
    pairs: list[tuple[str, str]] = []
    for key, values in qs.items():
        for value in values:
            pairs.append((key, value))
    return urlunparse(parsed._replace(query=urlencode(pairs)))


def _is_file_share(url: str) -> bool:
    host = hostname(url)
    if host.endswith("dropboxusercontent.com"):
        return True
    path = urlparse(url).path.lower()
    return any(path.startswith(prefix) for prefix in _FILE_PREFIXES)


class DropboxProvider(Provider):
    name = "dropbox"
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
        host = hostname(url)
        if not host:
            return False
        return (
            host in {"dropbox.com", "www.dropbox.com", "dl.dropbox.com"}
            or host.endswith(".dropbox.com")
            or host.endswith("dropboxusercontent.com")
        )

    def _downloadable_url(self, url: str) -> str:
        if not _is_file_share(url):
            raise ProviderNotConfiguredError(
                f"{self.name} (folder shares and non-file pages need Dropbox API; "
                "use a shared file link with dl=1)"
            )
        return force_download_url(url)

    def metadata(self, url: str) -> MediaMetadata:
        download_url = self._downloadable_url(url)
        path_name = unquote(urlparse(url).path.rsplit("/", 1)[-1] or "dropbox-file")
        # Strip query-looking crumbs from path segment
        title = path_name.split("?")[0] or "Dropbox file"
        content_type = head_content_type(download_url)
        ext = extension_from_url(url, default="bin")
        if "." in title:
            ext = title.rsplit(".", 1)[-1].lower() or ext
        fmt = FormatInfo(
            id="original",
            quality="original",
            container=ext,
            mime_type=content_type,
            url=download_url,
        )
        manifest = Manifest(
            type="direct",
            provider=self.name,
            url=download_url,
            format_ids=[fmt.id],
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=title,
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
        suffix = f".{fmt.container}" if fmt.container and fmt.container != "bin" else ""
        target = dest if dest.suffix else dest.with_suffix(suffix or dest.suffix)
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
