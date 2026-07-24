"""Platform module base — catalog platforms with direct-media download support."""

from __future__ import annotations

from pathlib import Path

from packages.core.exceptions import ProviderNotConfiguredError
from packages.core.models import (
    DownloadResult,
    FormatInfo,
    LiveInfo,
    Manifest,
    MediaMetadata,
    ProviderCapabilities,
    SubtitleTrack,
    ThumbnailInfo,
)
from packages.core.parser import hostname, is_direct_media_url
from packages.core.provider import Provider
from providers.direct_media import direct_download, direct_metadata


class PlatformModule(Provider):
    """Catalog platform module.

    - Host detection via ``host_suffixes``
    - Direct media URLs (``.mp4``, ``.m3u8``, …) → metadata + download
    - Page/watch URLs → ``ProviderNotConfiguredError`` until official API is wired
    """

    name: str = "module"
    status: str = "not_configured"
    host_suffixes: tuple[str, ...] = ()
    ie_names: tuple[str, ...] = ()
    source: str = "catalog"
    description: str = ""
    capabilities: ProviderCapabilities = ProviderCapabilities(
        metadata=True,
        manifest=True,
        formats=True,
        download=True,
        thumbnail=False,
        subtitle=False,
        live=False,
    )

    def supports(self, url: str) -> bool:
        if not self.host_suffixes:
            return False
        host = hostname(url)
        if not host:
            return False
        return any(host == suffix or host.endswith("." + suffix) for suffix in self.host_suffixes)

    def _require_direct_or_raise(self, url: str) -> None:
        if is_direct_media_url(url):
            return
        raise ProviderNotConfiguredError(self.name)

    def metadata(self, url: str) -> MediaMetadata:
        self._require_direct_or_raise(url)
        return direct_metadata(self.name, url)

    def manifest(self, url: str) -> Manifest:
        meta = self.metadata(url)
        if isinstance(meta.manifest, Manifest):
            return meta.manifest
        return Manifest(
            type="direct",
            provider=self.name,
            url=url,
            format_ids=[f.id for f in meta.formats],
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        self._require_direct_or_raise(url)
        return direct_download(self.name, url, format_id, dest)

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        if is_direct_media_url(url):
            return None
        raise ProviderNotConfiguredError(self.name)

    def subtitles(self, url: str) -> list[SubtitleTrack]:
        if is_direct_media_url(url):
            return []
        raise ProviderNotConfiguredError(self.name)

    def live(self, url: str) -> LiveInfo | None:
        if is_direct_media_url(url):
            return None
        raise ProviderNotConfiguredError(self.name)

    def get_metadata(self, url: str) -> MediaMetadata:
        return self.metadata(url)

    def list_formats(self, url: str) -> list[FormatInfo]:
        return self.formats(url)
