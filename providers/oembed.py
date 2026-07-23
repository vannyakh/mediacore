"""Shared helpers for public oEmbed metadata providers."""

from __future__ import annotations

from typing import Any

import httpx

from packages.core.exceptions import ProviderError
from packages.core.models import FormatInfo, Manifest, MediaMetadata

USER_AGENT = "MediaCore/0.1"


def fetch_oembed(
    endpoint: str,
    url: str,
    *,
    provider_name: str,
    timeout: float = 30.0,
    params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    query = {"url": url, **(params or {})}
    try:
        with httpx.Client(timeout=timeout, follow_redirects=True) as client:
            response = client.get(
                endpoint,
                params=query,
                headers={"User-Agent": USER_AGENT},
            )
            if response.status_code == 404:
                raise ProviderError(provider_name, "Media not found or not publicly embeddable")
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPError as exc:
        raise ProviderError(provider_name, f"oEmbed request failed: {exc}") from exc
    if not isinstance(data, dict):
        raise ProviderError(provider_name, "oEmbed response was not a JSON object")
    return data


def metadata_from_oembed(
    provider_name: str,
    url: str,
    data: dict[str, Any],
    *,
    title_fallback: str,
) -> MediaMetadata:
    fmt = FormatInfo(id="oembed", quality="preview", container="html")
    manifest = Manifest(
        type="oembed",
        provider=provider_name,
        url=url,
        format_ids=[fmt.id],
        extra={"provider_url": data.get("provider_url")},
    )
    duration = data.get("duration")
    if duration is not None:
        try:
            duration = float(duration)
        except (TypeError, ValueError):
            duration = None
    return MediaMetadata(
        platform=provider_name,
        url=url,
        title=data.get("title") or title_fallback,
        duration=duration,
        thumbnail=data.get("thumbnail_url"),
        description=data.get("description"),
        author=data.get("author_name"),
        formats=[fmt],
        manifest=manifest,
        extra={"html": data.get("html"), "type": data.get("type")},
    )
