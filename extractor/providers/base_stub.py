"""Shared stub provider for platforms awaiting official API credentials."""

from __future__ import annotations

from pathlib import Path

from extractor.core.base import Provider
from extractor.core.exceptions import ProviderNotConfiguredError
from extractor.core.models import DownloadResult, FormatInfo, VideoMetadata
from extractor.core.parser import hostname


class StubProvider(Provider):
    name: str = "stub"
    status: str = "not_configured"
    host_suffixes: tuple[str, ...] = ()

    def supports(self, url: str) -> bool:
        host = hostname(url)
        return any(host == suffix or host.endswith("." + suffix) for suffix in self.host_suffixes)

    def get_metadata(self, url: str) -> VideoMetadata:
        raise ProviderNotConfiguredError(self.name)

    def list_formats(self, url: str) -> list[FormatInfo]:
        raise ProviderNotConfiguredError(self.name)

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(self.name)
