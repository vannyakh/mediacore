"""Thin FFmpeg CLI wrapper for media processing plugins."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


class FFmpegError(RuntimeError):
    pass


def ffmpeg_available() -> bool:
    return shutil.which("ffmpeg") is not None


def probe_duration(path: Path) -> float | None:
    if not shutil.which("ffprobe"):
        return None
    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                str(path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        return float(result.stdout.strip())
    except (subprocess.CalledProcessError, ValueError):
        return None


def extract_thumbnail(source: Path, dest: Path, *, at_seconds: float = 1.0) -> Path:
    if not ffmpeg_available():
        raise FFmpegError("ffmpeg is not installed")
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-y",
        "-ss",
        str(at_seconds),
        "-i",
        str(source),
        "-frames:v",
        "1",
        str(dest),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise FFmpegError(result.stderr.strip() or "ffmpeg thumbnail failed")
    return dest


def extract_audio(source: Path, dest: Path, *, codec: str = "mp3") -> Path:
    if not ffmpeg_available():
        raise FFmpegError("ffmpeg is not installed")
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["ffmpeg", "-y", "-i", str(source), "-vn", "-acodec", "libmp3lame", str(dest)]
    if codec != "mp3":
        cmd = ["ffmpeg", "-y", "-i", str(source), "-vn", str(dest)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise FFmpegError(result.stderr.strip() or "ffmpeg audio extraction failed")
    return dest


def convert_media(source: Path, dest: Path) -> Path:
    if not ffmpeg_available():
        raise FFmpegError("ffmpeg is not installed")
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["ffmpeg", "-y", "-i", str(source), str(dest)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise FFmpegError(result.stderr.strip() or "ffmpeg convert failed")
    return dest


def download_stream(
    url: str,
    dest: Path,
    *,
    headers: dict[str, str] | None = None,
    timeout_sec: int = 600,
) -> Path:
    """
    Fetch a direct HLS/DASH (or ffmpeg-readable) stream URL into a local file.

    Requires ffmpeg. Does not scrape watch pages — pass a permitted media/playlist URL.
    """
    if not ffmpeg_available():
        raise FFmpegError(
            "ffmpeg is not installed (required for HLS/m3u8 and DASH stream download)"
        )
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.suffix:
        dest = dest.with_suffix(".mp4")

    def _build(extra: list[str]) -> list[str]:
        cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
        if headers:
            header_blob = "".join(f"{k}: {v}\r\n" for k, v in headers.items())
            cmd.extend(["-headers", header_blob])
        cmd.extend(["-i", url, *extra, str(dest)])
        return cmd

    attempts = (
        ["-c", "copy"],
        ["-c", "copy", "-bsf:a", "aac_adtstoasc"],  # MPEG-TS HLS → MP4
    )
    last_err = ""
    for extra in attempts:
        result = subprocess.run(
            _build(extra),
            capture_output=True,
            text=True,
            timeout=timeout_sec,
        )
        if result.returncode == 0 and dest.exists() and dest.stat().st_size > 0:
            return dest
        last_err = result.stderr.strip() or "ffmpeg stream download failed"
    raise FFmpegError(last_err)
