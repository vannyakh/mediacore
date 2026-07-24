"""Direct HLS/DASH playlist download via ffmpeg."""

from __future__ import annotations

from pathlib import Path

from packages.core.exceptions import DownloadError


def download_stream_file(
    url: str,
    dest: Path,
    *,
    headers: dict[str, str] | None = None,
) -> tuple[int, str | None]:
    """Download a direct HLS/DASH playlist URL via ffmpeg into a media file."""
    from packages.media.wrapper import FFmpegError, download_stream

    try:
        path = download_stream(url, dest, headers=headers)
    except FFmpegError as exc:
        raise DownloadError(str(exc)) from exc
    size = path.stat().st_size if path.exists() else 0
    return size, "video/mp4"


def looks_like_playlist_content_type(content_type: str | None) -> bool:
    if not content_type:
        return False
    ct = content_type.lower()
    return (
        "mpegurl" in ct
        or "m3u8" in ct
        or "dash+xml" in ct
        or ct.startswith("application/vnd.apple.mpegurl")
    )
