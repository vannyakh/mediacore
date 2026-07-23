"""URL parsing helpers."""

from __future__ import annotations

from urllib.parse import parse_qs, urlparse


def hostname(url: str) -> str:
    return (urlparse(url).hostname or "").lower()


def path_segments(url: str) -> list[str]:
    path = urlparse(url).path.strip("/")
    return [p for p in path.split("/") if p]


def query_param(url: str, key: str) -> str | None:
    values = parse_qs(urlparse(url).query).get(key)
    return values[0] if values else None


def is_direct_media_url(url: str) -> bool:
    path = urlparse(url).path.lower()
    return path.endswith(
        (
            ".mp4",
            ".webm",
            ".mkv",
            ".mov",
            ".m4v",
            ".mp3",
            ".m4a",
            ".aac",
            ".ogg",
            ".wav",
            ".flac",
            ".m3u8",
        )
    )
