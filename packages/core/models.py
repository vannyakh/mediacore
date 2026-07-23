"""Shared domain models."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class FormatInfo:
    id: str
    quality: str
    container: str
    mime_type: str | None = None
    filesize: int | None = None
    width: int | None = None
    height: int | None = None
    fps: float | None = None
    bitrate: int | None = None
    url: str | None = None
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "quality": self.quality,
            "container": self.container,
            "mime_type": self.mime_type,
            "filesize": self.filesize,
            "width": self.width,
            "height": self.height,
            "fps": self.fps,
            "bitrate": self.bitrate,
        }


@dataclass(slots=True)
class MediaMetadata:
    platform: str
    url: str
    title: str
    duration: float | None = None
    thumbnail: str | None = None
    description: str | None = None
    author: str | None = None
    formats: list[FormatInfo] = field(default_factory=list)
    manifest: dict[str, Any] | None = None
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "platform": self.platform,
            "url": self.url,
            "title": self.title,
            "duration": self.duration,
            "thumbnail": self.thumbnail,
            "description": self.description,
            "author": self.author,
            "formats": [f.to_dict() for f in self.formats],
            "manifest": self.manifest,
        }


# Back-compat
VideoMetadata = MediaMetadata


@dataclass(slots=True)
class DownloadResult:
    path: Path
    format_id: str
    container: str
    filesize: int | None = None
    content_type: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": str(self.path),
            "format_id": self.format_id,
            "container": self.container,
            "filesize": self.filesize,
            "content_type": self.content_type,
        }
