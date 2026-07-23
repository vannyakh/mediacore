"""Shared domain models for the MediaCore provider architecture."""

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
class Manifest:
    """Playback / delivery manifest for a media resource."""

    type: str
    provider: str
    url: str | None = None
    format_ids: list[str] = field(default_factory=list)
    is_live: bool = False
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "type": self.type,
            "provider": self.provider,
            "url": self.url,
            "format_ids": list(self.format_ids),
            "is_live": self.is_live,
            "extra": self.extra,
        }


@dataclass(slots=True)
class ThumbnailInfo:
    url: str | None = None
    width: int | None = None
    height: int | None = None
    path: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
            "width": self.width,
            "height": self.height,
            "path": self.path,
        }


@dataclass(slots=True)
class SubtitleTrack:
    id: str
    language: str
    label: str | None = None
    format: str = "vtt"
    url: str | None = None
    content: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "language": self.language,
            "label": self.label,
            "format": self.format,
            "url": self.url,
        }


@dataclass(slots=True)
class LiveInfo:
    """Live stream state when the provider supports Live."""

    is_live: bool
    status: str = "unknown"  # live | ended | scheduled | unknown
    stream_url: str | None = None
    started_at: str | None = None
    viewer_count: int | None = None
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "is_live": self.is_live,
            "status": self.status,
            "stream_url": self.stream_url,
            "started_at": self.started_at,
            "viewer_count": self.viewer_count,
            "extra": self.extra,
        }


@dataclass(slots=True)
class ProviderCapabilities:
    metadata: bool = True
    manifest: bool = True
    formats: bool = True
    download: bool = False
    thumbnail: bool = False
    subtitle: bool = False
    live: bool = False

    def to_list(self) -> list[str]:
        return [
            name
            for name in (
                "metadata",
                "manifest",
                "formats",
                "download",
                "thumbnail",
                "subtitle",
                "live",
            )
            if getattr(self, name)
        ]

    def to_dict(self) -> dict[str, bool]:
        return {
            "metadata": self.metadata,
            "manifest": self.manifest,
            "formats": self.formats,
            "download": self.download,
            "thumbnail": self.thumbnail,
            "subtitle": self.subtitle,
            "live": self.live,
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
    manifest: dict[str, Any] | Manifest | None = None
    is_live: bool = False
    subtitles: list[SubtitleTrack] = field(default_factory=list)
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manifest = self.manifest
        if isinstance(manifest, Manifest):
            manifest = manifest.to_dict()
        return {
            "platform": self.platform,
            "url": self.url,
            "title": self.title,
            "duration": self.duration,
            "thumbnail": self.thumbnail,
            "description": self.description,
            "author": self.author,
            "formats": [f.to_dict() for f in self.formats],
            "manifest": manifest,
            "is_live": self.is_live,
            "subtitles": [s.to_dict() for s in self.subtitles],
        }


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
