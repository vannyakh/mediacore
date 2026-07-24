"""ABC Australia provider using the public iView catalog API (metadata only)."""

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

# Catalog module name — keep identical so registry skips the stub.
PROVIDER_NAME = "abc.net.au"
SHOW_API = "https://api.iview.abc.net.au/v2/show/{slug}"
_SHOW_PATH = re.compile(r"^/show/(?P<slug>[^/]+)/?(?:series/\d+)?/?$", re.IGNORECASE)


class AbcNetAuProvider(Provider):
    name = PROVIDER_NAME
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
        return host in {"abc.net.au", "www.abc.net.au", "iview.abc.net.au"} or (
            host.endswith(".abc.net.au") if host else False
        )

    def metadata(self, url: str) -> MediaMetadata:
        slug = self._show_slug(url)
        if not slug:
            raise ProviderNotConfiguredError(
                f"{self.name} (page/video URLs need permitted access; "
                "iView show pages use the public catalog API)"
            )

        endpoint = SHOW_API.format(slug=slug)
        try:
            with httpx.Client(timeout=30.0, follow_redirects=True) as client:
                response = client.get(
                    endpoint,
                    headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
                )
                if response.status_code == 404:
                    raise ProviderError(self.name, "Show not found in iView catalog")
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPError as exc:
            raise ProviderError(self.name, f"iView catalog request failed: {exc}") from exc

        if not isinstance(data, dict):
            raise ProviderError(self.name, "iView catalog response was not a JSON object")

        title = data.get("displayTitle") or data.get("title") or slug
        thumb = data.get("thumbnail")
        fmt = FormatInfo(id="iview_show", quality="preview", container="html")
        manifest = Manifest(
            type="iview_show",
            provider=self.name,
            url=url,
            format_ids=[fmt.id],
            extra={"slug": data.get("slug") or slug, "show_id": data.get("id")},
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=title,
            thumbnail=thumb if isinstance(thumb, str) else None,
            description=data.get("description"),
            formats=[fmt],
            manifest=manifest,
            extra={
                "type": data.get("type"),
                "share_url": data.get("shareUrl"),
                "requires_login": data.get("requiresLogin"),
            },
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (download requires permitted ABC / geo-eligible access)"
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)

    def _show_slug(self, url: str) -> str | None:
        parsed = urlparse(url)
        host = (parsed.hostname or "").lower()
        if host not in {"iview.abc.net.au"} and not host.endswith(".iview.abc.net.au"):
            return None
        match = _SHOW_PATH.match(parsed.path or "")
        if not match:
            return None
        return match.group("slug")
