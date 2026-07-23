"""Stub provider for platforms awaiting permitted/official access."""

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
from packages.core.parser import hostname
from packages.core.provider import Provider


class StubProvider(Provider):
    name: str = "stub"
    status: str = "not_configured"
    host_suffixes: tuple[str, ...] = ()
    ie_names: tuple[str, ...] = ()
    source: str = "catalog"
    description: str = ""
    capabilities: ProviderCapabilities = ProviderCapabilities(
        metadata=False,
        manifest=False,
        formats=False,
        download=False,
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

    def metadata(self, url: str) -> MediaMetadata:
        raise ProviderNotConfiguredError(self.name)

    def manifest(self, url: str) -> Manifest:
        raise ProviderNotConfiguredError(self.name)

    def formats(self, url: str) -> list[FormatInfo]:
        raise ProviderNotConfiguredError(self.name)

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(self.name)

    def thumbnail(self, url: str) -> ThumbnailInfo | None:
        raise ProviderNotConfiguredError(self.name)

    def subtitles(self, url: str) -> list[SubtitleTrack]:
        raise ProviderNotConfiguredError(self.name)

    def live(self, url: str) -> LiveInfo | None:
        raise ProviderNotConfiguredError(self.name)

    # Keep old names working
    def get_metadata(self, url: str) -> MediaMetadata:
        return self.metadata(url)

    def list_formats(self, url: str) -> list[FormatInfo]:
        return self.formats(url)
