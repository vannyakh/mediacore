"""Fake provider implementing the MediaCore Provider contract."""

from __future__ import annotations

from pathlib import Path

from packages.core.exceptions import FormatNotFoundError
from packages.core.models import DownloadResult, FormatInfo, MediaMetadata
from packages.core.provider import Provider


class FakeProvider(Provider):
    name = "fake"
    status = "active"

    def __init__(
        self,
        *,
        prefix: str = "https://fake.mediacore.test/",
        title: str = "Fake Media",
        payload: bytes = b"fake-media-bytes",
        download_enabled: bool = True,
    ) -> None:
        self.prefix = prefix
        self.title = title
        self.payload = payload
        self.download_enabled = download_enabled
        self.calls: list[str] = []

    def supports(self, url: str) -> bool:
        return url.startswith(self.prefix)

    def get_metadata(self, url: str) -> MediaMetadata:
        self.calls.append("get_metadata")
        return MediaMetadata(
            platform=self.name,
            url=url,
            title=self.title,
            duration=1.0,
            formats=[
                FormatInfo(
                    id="original",
                    quality="original",
                    container="mp4",
                    mime_type="video/mp4",
                ),
            ],
            manifest={"type": "fake"},
        )

    def list_formats(self, url: str) -> list[FormatInfo]:
        self.calls.append("list_formats")
        return self.get_metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        self.calls.append("download")
        if not self.download_enabled:
            raise FormatNotFoundError(format_id)
        meta = self.get_metadata(url)
        fmt = next((f for f in meta.formats if f.id == format_id), None)
        if fmt is None:
            raise FormatNotFoundError(format_id)
        target = dest if dest.suffix else dest.with_suffix(".mp4")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(self.payload)
        return DownloadResult(
            path=target,
            format_id=fmt.id,
            container=fmt.container,
            filesize=len(self.payload),
            content_type="video/mp4",
        )
