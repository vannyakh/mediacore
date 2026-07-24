"""media.ccc.de provider via the public JSON API (metadata + recording download)."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

import httpx

from packages.core.downloader import download_file
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
from providers.oembed import USER_AGENT

API_BASE = "https://api.media.ccc.de/public/events"
_SLUG = re.compile(r"/v/(?P<slug>[^/?#]+)", re.I)


class MediaCccDeProvider(Provider):
    name = "media.ccc.de"
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
        return host in {"media.ccc.de", "api.media.ccc.de"}

    def _event_key(self, url: str) -> str:
        parsed = urlparse(url)
        match = _SLUG.search(parsed.path)
        if match:
            return match.group("slug")
        # Allow direct /public/events/{id|guid|slug}
        parts = [p for p in parsed.path.split("/") if p]
        if "events" in parts:
            idx = parts.index("events")
            if idx + 1 < len(parts):
                return parts[idx + 1]
        raise ProviderNotConfiguredError(
            f"{self.name} (need a talk URL like https://media.ccc.de/v/<slug>)"
        )

    def _fetch_event(self, key: str) -> dict:
        try:
            with httpx.Client(timeout=30.0, follow_redirects=True) as client:
                response = client.get(
                    f"{API_BASE}/{key}",
                    headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
                )
                if response.status_code == 404:
                    raise ProviderError(self.name, f"Event not found: {key}")
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPError as exc:
            raise ProviderError(self.name, f"media.ccc.de API request failed: {exc}") from exc
        if not isinstance(data, dict):
            raise ProviderError(self.name, "Unexpected media.ccc.de API response")
        return data

    def metadata(self, url: str) -> MediaMetadata:
        key = self._event_key(url)
        data = self._fetch_event(key)
        formats: list[FormatInfo] = []
        for recording in data.get("recordings") or []:
            if not isinstance(recording, dict):
                continue
            rec_url = recording.get("recording_url") or recording.get("url")
            if not isinstance(rec_url, str) or not rec_url:
                continue
            folder = str(recording.get("folder") or "original")
            language = str(recording.get("language") or "")
            fmt_id = "-".join(p for p in (language, folder) if p) or "original"
            mime = str(recording.get("mime_type") or "")
            container = "mp4"
            if "webm" in mime or folder.endswith("webm"):
                container = "webm"
            elif "mp3" in mime or folder == "mp3":
                container = "mp3"
            elif "opus" in mime or folder == "opus":
                container = "opus"
            height = recording.get("height")
            quality = f"{height}p" if height else folder
            formats.append(
                FormatInfo(
                    id=fmt_id,
                    quality=quality,
                    container=container,
                    mime_type=mime or None,
                    url=rec_url,
                    height=int(height) if isinstance(height, int) else None,
                    width=int(recording["width"]) if isinstance(recording.get("width"), int) else None,
                )
            )
        if not formats:
            raise ProviderNotConfiguredError(
                f"{self.name} (no public recordings listed for this event)"
            )
        length = data.get("length")
        try:
            duration = float(length) if length is not None else None
        except (TypeError, ValueError):
            duration = None
        persons = data.get("persons") or []
        author = ", ".join(str(p) for p in persons) if isinstance(persons, list) else None
        manifest = Manifest(
            type="media_ccc_de",
            provider=self.name,
            url=url,
            format_ids=[f.id for f in formats],
            extra={"guid": data.get("guid"), "slug": data.get("slug")},
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=str(data.get("title") or key),
            duration=duration,
            thumbnail=data.get("thumb_url") if isinstance(data.get("thumb_url"), str) else None,
            description=data.get("description") if isinstance(data.get("description"), str) else None,
            author=author,
            formats=formats,
            manifest=manifest,
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        meta = self.metadata(url)
        fmt = next((f for f in meta.formats if f.id == format_id or f.quality == format_id), None)
        if fmt is None and format_id == "original" and meta.formats:
            fmt = meta.formats[0]
        if fmt is None or not fmt.url:
            raise FormatNotFoundError(format_id)
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
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)
