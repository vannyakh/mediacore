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
