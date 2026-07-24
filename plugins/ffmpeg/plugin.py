"""FFmpeg plugin — gates availability and exposes media helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from packages.media import wrapper as media

PLUGIN = {
    "name": "mediacore-plugin-ffmpeg",
    "version": "0.1.0",
    "kind": "ffmpeg",
    "description": "FFmpeg-powered convert, audio extract, thumbnail, and clip",
    "status": "available",
    "capabilities": ["convert", "audio", "thumbnail", "clip", "probe"],
}


class FFmpegService:
    def available(self) -> bool:
        return media.ffmpeg_available()

    def extract_audio(self, source: Path, dest: Path, *, codec: str = "mp3") -> Path:
        return media.extract_audio(source, dest, codec=codec)

    def extract_thumbnail(
        self, source: Path, dest: Path, *, at_seconds: float = 1.0
    ) -> Path:
        return media.extract_thumbnail(source, dest, at_seconds=at_seconds)

    def convert(self, source: Path, dest: Path) -> Path:
        return media.convert_media(source, dest)

    def probe_duration(self, path: Path) -> float | None:
        return media.probe_duration(path)


def create(settings: Any | None = None) -> FFmpegService:
    del settings
    return FFmpegService()
