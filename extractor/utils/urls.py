"""URL helpers (compat shim under extractor.utils)."""

from __future__ import annotations

from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    return url.strip()


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
