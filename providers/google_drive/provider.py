"""Google Drive provider — public shared files via ``uc?export=download&id=``."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

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
from packages.core.parser import hostname
from packages.core.provider import Provider

_FILE_ID_RE = re.compile(r"/file/d/([a-zA-Z0-9_-]+)")
_DOCS_ID_RE = re.compile(
    r"/(?:document|spreadsheets|presentation)/d/([a-zA-Z0-9_-]+)"
)


def extract_file_id(url: str) -> str | None:
    parsed = urlparse(url)
    match = _FILE_ID_RE.search(parsed.path)
    if match:
        return match.group(1)
    docs = _DOCS_ID_RE.search(parsed.path)
    if docs:
        return docs.group(1)
    qs = parse_qs(parsed.query)
    for key in ("id", "file_id"):
        if key in qs and qs[key]:
            return qs[key][0]
    return None


def export_download_url(file_id: str) -> str:
    # confirm=t helps skip the interstitial on larger public files.
    return f"https://drive.google.com/uc?export=download&id={file_id}&confirm=t"


class GoogleDriveProvider(Provider):
    name = "google_drive"
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
        return host in {
            "drive.google.com",
            "docs.google.com",
            "drive.usercontent.google.com",
        }

    def _file_id(self, url: str) -> str:
        file_id = extract_file_id(url)
        if not file_id:
            raise ProviderNotConfiguredError(
                f"{self.name} (need a public file share link with a file id; "
                "folders and private files require Google Drive API credentials)"
            )
        path = urlparse(url).path.lower()
        if "/folders/" in path:
            raise ProviderNotConfiguredError(
                f"{self.name} (folder shares require Google Drive API credentials)"
            )
        return file_id

    def metadata(self, url: str) -> MediaMetadata:
        file_id = self._file_id(url)
        download_url = export_download_url(file_id)
        path_name = unquote(urlparse(url).path.rsplit("/", 1)[-1] or file_id)
        title = path_name if path_name not in {"view", "edit", "preview"} else file_id
        content_type = head_content_type(download_url)
        fmt = FormatInfo(
            id="original",
            quality="original",
            container="bin",
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
        target = dest if dest.suffix else dest.with_suffix(".bin")
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
