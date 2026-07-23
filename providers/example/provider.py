"""Example provider demonstrating the MediaCore provider interface."""

from __future__ import annotations

from pathlib import Path

from packages.core.exceptions import ProviderNotConfiguredError
from packages.core.models import DownloadResult, FormatInfo, MediaMetadata
from packages.core.provider import Provider


class ExampleProvider(Provider):
    name = "example"
    status = "example"

    def supports(self, url: str) -> bool:
        return url.startswith("mediacore://example/")

    def get_metadata(self, url: str) -> MediaMetadata:
        return MediaMetadata(
            platform=self.name,
            url=url,
            title="Example Media",
            duration=12.0,
            formats=[
                FormatInfo(id="demo", quality="720p", container="mp4"),
            ],
            manifest={"type": "example"},
        )

    def list_formats(self, url: str) -> list[FormatInfo]:
        return self.get_metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        raise ProviderNotConfiguredError(
            f"{self.name} (demo provider — no real media payload)"
        )
