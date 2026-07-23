"""Wikimedia provider using the public MediaWiki REST summary API (metadata only)."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlparse

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

# Catalog stub name is `wikimedia.org` — keep the same name so registry skips the stub.
PROVIDER_NAME = "wikimedia.org"


class WikimediaProvider(Provider):
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
        return host == "wikimedia.org" or host.endswith(".wikimedia.org")

    def metadata(self, url: str) -> MediaMetadata:
        summary_url = self._summary_endpoint(url)
        try:
            with httpx.Client(timeout=30.0, follow_redirects=True) as client:
                response = client.get(
                    summary_url,
                    headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
                )
                if response.status_code == 404:
                    raise ProviderError(self.name, "Page not found or not publicly available")
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPError as exc:
            raise ProviderError(self.name, f"Wikimedia API request failed: {exc}") from exc

        if not isinstance(data, dict):
            raise ProviderError(self.name, "Wikimedia API response was not a JSON object")

        thumb = None
        thumbnail = data.get("thumbnail") or {}
        if isinstance(thumbnail, dict):
            thumb = thumbnail.get("source")
        original = data.get("originalimage") or {}
        if not thumb and isinstance(original, dict):
            thumb = original.get("source")

        fmt = FormatInfo(id="summary", quality="preview", container="html")
        manifest = Manifest(
            type="wikimedia_summary",
            provider=self.name,
            url=url,
            format_ids=[fmt.id],
            extra={"content_urls": data.get("content_urls")},
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=data.get("title") or data.get("displaytitle") or "Wikimedia media",
            thumbnail=thumb,
            description=data.get("extract") or data.get("description"),
            author=None,
            formats=[fmt],
            manifest=manifest,
            extra={"type": data.get("type"), "lang": data.get("lang")},
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (download requires permitted Wikimedia content access)"
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)

    def _summary_endpoint(self, url: str) -> str:
        parsed = urlparse(url)
        host = (parsed.hostname or "commons.wikimedia.org").lower()
        path = unquote(parsed.path or "")

        # /wiki/Title → REST summary
        if "/wiki/" in path:
            title = path.split("/wiki/", 1)[1].strip("/")
            if title:
                return f"https://{host}/api/rest_v1/page/summary/{title}"

        # upload.wikimedia.org/.../FileName.ext → commons File: summary
        if host.startswith("upload."):
            filename = path.rstrip("/").rsplit("/", 1)[-1]
            if filename:
                return (
                    "https://commons.wikimedia.org/api/rest_v1/page/summary/"
                    f"File:{filename}"
                )

        raise ProviderError(
            self.name,
            "URL is not a Wikimedia wiki page or upload file path",
        )
