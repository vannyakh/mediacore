"""Internet Archive provider via public metadata API + /download/ file URLs."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote, unquote, urlparse

import httpx

from packages.core.downloader import download_file
from packages.core.exceptions import FormatNotFoundError, ProviderError, ProviderNotConfiguredError
from packages.core.format_select import select_format_id
from packages.core.models import (
    DownloadResult,
    FormatInfo,
    Manifest,
    MediaMetadata,
    ProviderCapabilities,
    ThumbnailInfo,
)
from packages.core.networking import create_client
from packages.core.parser import hostname
from packages.core.provider import Provider
from providers.oembed import USER_AGENT

_ID_RE = re.compile(
    r"/(?:details|download|metadata|stream)/(?P<id>[^/?#]+)",
    re.I,
)
_MEDIA_EXT = {
    "mp4",
    "webm",
    "mkv",
    "avi",
    "mov",
    "ogv",
    "mp3",
    "ogg",
    "oga",
    "flac",
    "wav",
    "m4a",
    "aac",
    "opus",
    "pdf",
    "epub",
}


class ArchiveorgProvider(Provider):
    name = "archiveorg"
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
        return host in {"archive.org", "www.archive.org"}

    def _identifier(self, url: str) -> str:
        path = unquote(urlparse(url).path or "")
        match = _ID_RE.search(path)
        if match:
            return match.group("id")
        raise ProviderNotConfiguredError(
            f"{self.name} (need https://archive.org/details/<identifier>)"
        )

    def _fetch_metadata(self, identifier: str) -> dict:
        try:
            with create_client(timeout=30.0) as client:
                response = client.get(
                    f"https://archive.org/metadata/{identifier}",
                    headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
                )
                if response.status_code == 404:
                    raise ProviderError(self.name, f"Item not found: {identifier}")
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPError as exc:
            raise ProviderError(self.name, f"Internet Archive API failed: {exc}") from exc
        if not isinstance(data, dict):
            raise ProviderError(self.name, "Unexpected Internet Archive response")
        return data

    def _formats_from_files(self, identifier: str, files: list) -> list[FormatInfo]:
        formats: list[FormatInfo] = []
        seen: set[str] = set()
        for entry in files:
            if not isinstance(entry, dict):
                continue
            name = entry.get("name")
            if not isinstance(name, str) or not name:
                continue
            ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
            if ext not in _MEDIA_EXT:
                continue
            fmt_id = name
            if fmt_id in seen:
                continue
            seen.add(fmt_id)
            size_raw = entry.get("size")
            try:
                filesize = int(size_raw) if size_raw is not None else None
            except (TypeError, ValueError):
                filesize = None
            formats.append(
                FormatInfo(
                    id=fmt_id,
                    quality=str(entry.get("format") or ext),
                    container=ext,
                    filesize=filesize,
                    url=(
                        f"https://archive.org/download/{identifier}/"
                        f"{quote(name, safe='/')}"
                    ),
                    extra={"source": entry.get("source"), "format": entry.get("format")},
                )
            )
        return formats

    def metadata(self, url: str) -> MediaMetadata:
        identifier = self._identifier(url)
        data = self._fetch_metadata(identifier)
        meta = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
        files = data.get("files") if isinstance(data.get("files"), list) else []
        formats = self._formats_from_files(identifier, files)
        if not formats:
            raise ProviderNotConfiguredError(
                f"{self.name} (no public media files listed for {identifier})"
            )
        title = meta.get("title") or identifier
        thumb = f"https://archive.org/services/img/{identifier}"
        manifest = Manifest(
            type="archive_org",
            provider=self.name,
            url=f"https://archive.org/details/{identifier}",
            format_ids=[f.id for f in formats],
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=str(title),
            thumbnail=thumb,
            description=str(meta.get("description") or "") or None,
            author=(meta.get("creator") if isinstance(meta.get("creator"), str) else None),
            formats=formats,
            manifest=manifest,
            extra={"identifier": identifier, "mediatype": meta.get("mediatype")},
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        meta = self.metadata(url)
        chosen = next((f for f in meta.formats if f.id == format_id), None)
        if chosen is None and format_id in {"original", "best", "default"}:
            fid = select_format_id(meta.formats, format_id)
            chosen = next(f for f in meta.formats if f.id == fid)
        if chosen is None or not chosen.url:
            raise FormatNotFoundError(format_id)
        if not dest.suffix and "." in chosen.id:
            dest = dest.with_suffix("." + chosen.id.rsplit(".", 1)[-1])
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
