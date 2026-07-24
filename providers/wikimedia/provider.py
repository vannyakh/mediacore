"""Wikimedia provider via public MediaWiki REST summary API (metadata + original image)."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlparse

import httpx

from packages.core.downloader import download_file
from packages.core.exceptions import ProviderError, ProviderNotConfiguredError
from packages.core.models import (
    DownloadResult,
    FormatInfo,
    Manifest,
    MediaMetadata,
    ProviderCapabilities,
    ThumbnailInfo,
)
from packages.core.networking import create_client
from packages.core.parser import extension_from_url, hostname
from packages.core.provider import Provider
from providers.oembed import USER_AGENT

# Catalog stub name is `wikimedia.org` — keep the same name so registry skips the stub.
PROVIDER_NAME = "wikimedia.org"


class WikimediaProvider(Provider):
    name = PROVIDER_NAME
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
        return host == "wikimedia.org" or host.endswith(".wikimedia.org")

    def _fetch_summary(self, url: str) -> dict:
        summary_url = self._summary_endpoint(url)
        try:
            with create_client(timeout=30.0) as client:
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
        return data

    def metadata(self, url: str) -> MediaMetadata:
        data = self._fetch_summary(url)
        thumb = None
        thumbnail = data.get("thumbnail") or {}
        if isinstance(thumbnail, dict):
            thumb = thumbnail.get("source")
        original = data.get("originalimage") or {}
        original_url = original.get("source") if isinstance(original, dict) else None
        if not thumb and original_url:
            thumb = original_url

        formats: list[FormatInfo] = []
        if isinstance(original_url, str) and original_url:
            ext = extension_from_url(original_url) or "bin"
            formats.append(
                FormatInfo(
                    id="original",
                    quality="original",
                    container=ext.lstrip("."),
                    url=original_url,
                    width=int(original["width"]) if isinstance(original.get("width"), int) else None,
                    height=int(original["height"])
                    if isinstance(original.get("height"), int)
                    else None,
                )
            )
        if not formats:
            formats.append(FormatInfo(id="summary", quality="preview", container="html"))

        manifest = Manifest(
            type="wikimedia_summary",
            provider=self.name,
            url=url,
            format_ids=[f.id for f in formats],
            extra={"content_urls": data.get("content_urls")},
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=data.get("title") or data.get("displaytitle") or "Wikimedia media",
            thumbnail=thumb,
            description=data.get("extract") or data.get("description"),
            author=None,
            formats=formats,
            manifest=manifest,
            extra={"type": data.get("type"), "lang": data.get("lang")},
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        meta = self.metadata(url)
        chosen = next((f for f in meta.formats if f.id == format_id), None)
        if chosen is None and format_id in {"original", "best", "default"}:
            chosen = next((f for f in meta.formats if f.id == "original"), meta.formats[0])
        if chosen is None or not chosen.url:
            raise ProviderNotConfiguredError(
                f"{self.name} (no originalimage URL from public summary API — "
                "use a File: or upload.wikimedia.org URL)"
            )
        if chosen.id == "summary":
            raise ProviderNotConfiguredError(
                f"{self.name} (page has no downloadable original image)"
            )
        ext = chosen.container or extension_from_url(chosen.url) or "bin"
        if not dest.suffix:
            dest = dest.with_suffix("." + ext.lstrip("."))
        size, ctype = download_file(chosen.url, dest)
        return DownloadResult(
            path=dest,
            format_id=chosen.id,
            container=chosen.container or ext.lstrip("."),
            filesize=size,
            content_type=ctype,
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

        if "/wiki/" in path:
            title = path.split("/wiki/", 1)[1].strip("/")
            if title:
                return f"https://{host}/api/rest_v1/page/summary/{title}"

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
