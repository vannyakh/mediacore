"""BBC provider using public /programmes/{pid}.json (metadata only)."""

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

PROGRAMMES_JSON = "https://www.bbc.co.uk/programmes/{pid}.json"
_PROGRAMME_PATH = re.compile(
    r"^/programmes/(?P<pid>[pbmuw][0-9a-z]{7,})(?:/|$)",
    re.IGNORECASE,
)
_IMAGE = "https://ichef.bbci.co.uk/images/ic/960x540/{image_pid}.jpg"


class BbcProvider(Provider):
    name = "bbc"
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
        return host in {
            "bbc.co.uk",
            "www.bbc.co.uk",
            "bbc.com",
            "www.bbc.com",
        } or (bool(host) and host.endswith(".bbc.co.uk"))

    def metadata(self, url: str) -> MediaMetadata:
        pid = self._programme_pid(url)
        if not pid:
            raise ProviderNotConfiguredError(
                f"{self.name} (only /programmes/{{pid}} uses the public JSON feed; "
                "iPlayer/news pages need permitted access)"
            )

        endpoint = PROGRAMMES_JSON.format(pid=pid)
        try:
            with httpx.Client(timeout=30.0, follow_redirects=True) as client:
                response = client.get(
                    endpoint,
                    headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
                )
                if response.status_code == 404:
                    raise ProviderError(self.name, "Programme not found")
                response.raise_for_status()
                payload = response.json()
        except httpx.HTTPError as exc:
            raise ProviderError(self.name, f"BBC programmes request failed: {exc}") from exc

        programme = payload.get("programme") if isinstance(payload, dict) else None
        if not isinstance(programme, dict):
            raise ProviderError(self.name, "Unexpected BBC programmes response")

        title = programme.get("title") or programme.get("display_title") or pid
        if isinstance(title, dict):
            title = title.get("title") or pid
        description = (
            programme.get("short_synopsis")
            or programme.get("medium_synopsis")
            or programme.get("long_synopsis")
        )
        image = programme.get("image") if isinstance(programme.get("image"), dict) else {}
        image_pid = image.get("pid")
        thumb = _IMAGE.format(image_pid=image_pid) if image_pid else None

        ownership = programme.get("ownership") if isinstance(programme.get("ownership"), dict) else {}
        author = None
        if isinstance(ownership.get("service"), dict):
            author = ownership["service"].get("title")

        fmt = FormatInfo(id="programmes_json", quality="preview", container="html")
        manifest = Manifest(
            type="bbc_programmes",
            provider=self.name,
            url=url,
            format_ids=[fmt.id],
            extra={"pid": programme.get("pid") or pid, "type": programme.get("type")},
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=str(title),
            thumbnail=thumb,
            description=description if isinstance(description, str) else None,
            author=author if isinstance(author, str) else None,
            formats=[fmt],
            manifest=manifest,
            extra={"programme_type": programme.get("type")},
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (download requires permitted BBC / iPlayer access)"
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)

    def _programme_pid(self, url: str) -> str | None:
        parsed = urlparse(url)
        match = _PROGRAMME_PATH.match(parsed.path or "")
        if not match:
            return None
        return match.group("pid").lower()
