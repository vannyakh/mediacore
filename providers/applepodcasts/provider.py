"""Apple Podcasts provider using the public iTunes Lookup API (metadata only)."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse

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

LOOKUP_ENDPOINT = "https://itunes.apple.com/lookup"
_ID_IN_PATH = re.compile(r"/id(\d+)", re.IGNORECASE)


class ApplepodcastsProvider(Provider):
    name = "applepodcasts"
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
        return host in {"podcasts.apple.com", "itunes.apple.com"}

    def metadata(self, url: str) -> MediaMetadata:
        lookup_id = self._lookup_id(url)
        if not lookup_id:
            raise ProviderError(self.name, "Could not parse Apple Podcasts id from URL")

        try:
            with httpx.Client(timeout=30.0, follow_redirects=True) as client:
                response = client.get(
                    LOOKUP_ENDPOINT,
                    params={"id": lookup_id},
                    headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
                )
                response.raise_for_status()
                payload = response.json()
        except httpx.HTTPError as exc:
            raise ProviderError(self.name, f"iTunes Lookup request failed: {exc}") from exc

        results = payload.get("results") if isinstance(payload, dict) else None
        if not isinstance(results, list) or not results:
            raise ProviderError(self.name, "Podcast not found or not publicly listed")
        item = results[0]
        if not isinstance(item, dict):
            raise ProviderError(self.name, "Unexpected iTunes Lookup response")

        duration_ms = item.get("trackTimeMillis")
        duration = None
        if duration_ms is not None:
            try:
                duration = float(duration_ms) / 1000.0
            except (TypeError, ValueError):
                duration = None

        thumb = (
            item.get("artworkUrl600")
            or item.get("artworkUrl100")
            or item.get("artworkUrl60")
        )
        title = (
            item.get("trackName")
            or item.get("collectionName")
            or item.get("artistName")
            or "Apple Podcasts"
        )
        fmt = FormatInfo(id="itunes_lookup", quality="preview", container="html")
        manifest = Manifest(
            type="itunes_lookup",
            provider=self.name,
            url=url,
            format_ids=[fmt.id],
            extra={"lookup_id": lookup_id, "kind": item.get("kind")},
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=title,
            duration=duration,
            thumbnail=thumb if isinstance(thumb, str) else None,
            description=item.get("description") or item.get("collectionCensoredName"),
            author=item.get("artistName"),
            formats=[fmt],
            manifest=manifest,
            extra={
                "collection_id": item.get("collectionId"),
                "track_id": item.get("trackId"),
                "feed_url": item.get("feedUrl"),
            },
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (download requires permitted podcast / Apple Media Services access)"
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)

    def _lookup_id(self, url: str) -> str | None:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        # Episode query: ?i=<trackId>
        episode = (query.get("i") or [None])[0]
        if episode and str(episode).isdigit():
            return str(episode)
        match = _ID_IN_PATH.search(parsed.path or "")
        if match:
            return match.group(1)
        return None
