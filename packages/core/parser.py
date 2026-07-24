"""URL parsing helpers."""

from __future__ import annotations

from urllib.parse import parse_qs, urlparse


def normalize_url(url: str) -> str:
    return url.strip()


def hostname(url: str) -> str:
    return (urlparse(url).hostname or "").lower()


def path_segments(url: str) -> list[str]:
    path = urlparse(url).path.strip("/")
    return [p for p in path.split("/") if p]


def query_param(url: str, key: str) -> str | None:
    values = parse_qs(urlparse(url).query).get(key)
    return values[0] if values else None


def extension_from_url(url: str, default: str = "bin") -> str:
    path = urlparse(url).path
    if "." in path.rsplit("/", 1)[-1]:
        return path.rsplit(".", 1)[-1].lower()
    return default


def quality_from_height(height: int | None) -> str:
    if height is None:
        return "original"
    if height >= 2160:
        return "2160p"
    if height >= 1440:
        return "1440p"
    if height >= 1080:
        return "1080p"
    if height >= 720:
        return "720p"
    if height >= 480:
        return "480p"
    if height >= 360:
        return "360p"
    return f"{height}p"


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
