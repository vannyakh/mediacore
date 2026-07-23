"""Test data generators."""

from __future__ import annotations

from packages.core.models import FormatInfo, MediaMetadata


def make_format(format_id: str = "original", *, container: str = "mp4") -> FormatInfo:
    return FormatInfo(
        id=format_id,
        quality=format_id,
        container=container,
        mime_type=f"video/{container}",
    )


def make_metadata(
    *,
    platform: str = "generic",
    url: str = "https://cdn.example.com/demo.mp4",
    title: str = "demo.mp4",
) -> MediaMetadata:
    return MediaMetadata(
        platform=platform,
        url=url,
        title=title,
        formats=[make_format()],
        manifest={"type": "direct"},
    )


def make_huge_metadata(n_formats: int = 1000) -> MediaMetadata:
    formats = [make_format(f"f{i}", container="mp4") for i in range(n_formats)]
    return MediaMetadata(
        platform="stress",
        url="https://cdn.example.com/huge.mp4",
        title="huge",
        formats=formats,
        manifest={"formats": [f.id for f in formats]},
    )
