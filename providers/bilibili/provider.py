"""Bilibili provider using the public web view API (metadata only)."""

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

VIEW_API = "https://api.bilibili.com/x/web-interface/view"
_BV = re.compile(r"(?:/video/|bvid=)(?P<bvid>[bB][vV][0-9A-Za-z]+)")
_AV = re.compile(r"/video/[aA][vV](?P<aid>\d+)")


class BilibiliProvider(Provider):
    name = "bilibili"
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
            "bilibili.com",
            "www.bilibili.com",
            "space.bilibili.com",
            "player.bilibili.com",
            "live.bilibili.com",
            "b23.tv",
            "bilibili.tv",
            "www.bilibili.tv",
        } or (bool(host) and host.endswith(".bilibili.com"))

    def metadata(self, url: str) -> MediaMetadata:
        resolved = self._resolve_url(url)
        params = self._view_params(resolved)
        if not params:
            raise ProviderNotConfiguredError(
                f"{self.name} (only public video BV/av URLs use the view API; "
                "other pages need permitted access)"
            )

        try:
            with httpx.Client(timeout=30.0, follow_redirects=True) as client:
                response = client.get(
                    VIEW_API,
                    params=params,
                    headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
                )
                response.raise_for_status()
                payload = response.json()
        except httpx.HTTPError as exc:
            raise ProviderError(self.name, f"Bilibili view request failed: {exc}") from exc

        if not isinstance(payload, dict) or payload.get("code") != 0:
            message = payload.get("message") if isinstance(payload, dict) else "unknown"
            raise ProviderError(self.name, f"Bilibili view API error: {message}")
        data = payload.get("data")
        if not isinstance(data, dict):
            raise ProviderError(self.name, "Unexpected Bilibili view response")

        owner = data.get("owner") if isinstance(data.get("owner"), dict) else {}
        duration = data.get("duration")
        try:
            duration_f = float(duration) if duration is not None else None
        except (TypeError, ValueError):
            duration_f = None

        fmt = FormatInfo(id="bilibili_view", quality="preview", container="html")
        manifest = Manifest(
            type="bilibili_view",
            provider=self.name,
            url=url,
            format_ids=[fmt.id],
            extra={"bvid": data.get("bvid"), "aid": data.get("aid")},
        )
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=data.get("title") or "Bilibili video",
            duration=duration_f,
            thumbnail=data.get("pic") if isinstance(data.get("pic"), str) else None,
            description=data.get("desc") if isinstance(data.get("desc"), str) else None,
            author=owner.get("name") if isinstance(owner.get("name"), str) else None,
            formats=[fmt],
            manifest=manifest,
            extra={"aid": data.get("aid"), "bvid": data.get("bvid"), "cid": data.get("cid")},
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (download requires permitted Bilibili / content-owner access)"
        )

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        meta = self.metadata(url)
        if not meta.thumbnail:
            return None
        return ThumbnailInfo(url=meta.thumbnail)

    def _resolve_url(self, url: str) -> str:
        host = hostname(url)
        if host != "b23.tv":
            return url
        try:
            with httpx.Client(timeout=20.0, follow_redirects=True) as client:
                response = client.head(url, headers={"User-Agent": USER_AGENT})
                if response.status_code >= 400:
                    response = client.get(url, headers={"User-Agent": USER_AGENT})
                return str(response.url)
        except httpx.HTTPError:
            return url

    def _view_params(self, url: str) -> dict[str, str] | None:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        if query.get("bvid"):
            return {"bvid": query["bvid"][0]}
        if query.get("aid"):
            return {"aid": query["aid"][0]}
        text = f"{parsed.path}?{parsed.query}"
        bv = _BV.search(text)
        if bv:
            return {"bvid": bv.group("bvid")}
        av = _AV.search(parsed.path or "")
        if av:
            return {"aid": av.group("aid")}
        return None
