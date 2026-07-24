"""BitChute provider using the public beta video API (metadata only)."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

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
from providers.oembed import USER_AGENT

VIDEO_API = "https://api.bitchute.com/api/beta/video"
_VIDEO_PATH = re.compile(
    r"^/(?:video|embed|torrent/[^/]+)/(?P<id>[^/?#&]+)/?",
    re.IGNORECASE,
)


def _parse_duration(value: object) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if not isinstance(value, str):
        return None
    parts = value.strip().split(":")
    if not parts or not all(p.isdigit() for p in parts):
        return None
    nums = [int(p) for p in parts]
    if len(nums) == 3:
        h, m, s = nums
        return float(h * 3600 + m * 60 + s)
    if len(nums) == 2:
        m, s = nums
        return float(m * 60 + s)
    if len(nums) == 1:
        return float(nums[0])
    return None


class BitchuteProvider(Provider):
    name = "bitchute"
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
        return host in {"bitchute.com", "www.bitchute.com", "old.bitchute.com"} or (
            bool(host) and host.endswith(".bitchute.com")
        )

    def metadata(self, url: str) -> MediaMetadata:
        video_id = self._video_id(url)
        if not video_id:
            raise ProviderNotConfiguredError(
                f"{self.name} (only /video/{{id}} uses the public beta API; "
                "channel/playlist pages need permitted access)"
            )

        try:
            with httpx.Client(timeout=30.0, follow_redirects=True) as client:
                response = client.post(
                    VIDEO_API,
                    json={"video_id": video_id},
                    headers={
                        "User-Agent": USER_AGENT,
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                    },
                )
                if response.status_code == 404:
                    raise ProviderError(self.name, "Video not found")
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPError as exc:
            raise ProviderError(self.name, f"BitChute API request failed: {exc}") from exc

        if not isinstance(data, dict):
            raise ProviderError(self.name, "Unexpected BitChute API response")
        if data.get("errors"):
            raise ProviderError(self.name, "Video not found or not publicly available")

        channel = data.get("channel") if isinstance(data.get("channel"), dict) else {}
        author = channel.get("channel_name")
        fmt = FormatInfo(id="bitchute_api", quality="preview", container="html")
        manifest = Manifest(
            type="bitchute_video",
            provider=self.name,
            url=url,
            format_ids=[fmt.id],
            extra={"video_id": data.get("video_id") or video_id},
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=data.get("video_name") or video_id,
            duration=_parse_duration(data.get("duration")),
            thumbnail=data.get("thumbnail_url")
            if isinstance(data.get("thumbnail_url"), str)
            else None,
            description=data.get("description")
            if isinstance(data.get("description"), str)
            else None,
            author=author if isinstance(author, str) else None,
            formats=[fmt],
            manifest=manifest,
            extra={
                "video_id": data.get("video_id") or video_id,
                "view_count": data.get("view_count"),
                "date_published": data.get("date_published"),
            },
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (download requires permitted BitChute / content-owner access)"
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)

    def _video_id(self, url: str) -> str | None:
        parsed = urlparse(url)
        match = _VIDEO_PATH.match(parsed.path or "")
        if not match:
            return None
        return match.group("id").rstrip("/")
