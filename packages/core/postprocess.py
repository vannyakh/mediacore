"""Post-download processing chain (yt-dlp ``postprocessor`` analog)."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from packages.core.exceptions import PluginError
from packages.media.wrapper import FFmpegError, convert_media, extract_audio


class PostprocessStep(str, Enum):
    REMUX = "remux"
    EXTRACT_AUDIO = "extract_audio"


@dataclass
class PostprocessRequest:
    source: Path
    dest: Path
    step: PostprocessStep = PostprocessStep.REMUX
    audio_codec: str = "mp3"


def run_postprocess(req: PostprocessRequest) -> Path:
    """Run a single postprocess step on an already-downloaded file."""
    try:
        if req.step == PostprocessStep.EXTRACT_AUDIO:
            return extract_audio(req.source, req.dest, codec=req.audio_codec)
        return convert_media(req.source, req.dest)
    except FFmpegError as exc:
        raise PluginError(str(exc)) from exc


def remux(source: Path, dest: Path) -> Path:
    return run_postprocess(PostprocessRequest(source=source, dest=dest, step=PostprocessStep.REMUX))


def extract_audio_track(source: Path, dest: Path, *, codec: str = "mp3") -> Path:
    return run_postprocess(
        PostprocessRequest(
            source=source,
            dest=dest,
            step=PostprocessStep.EXTRACT_AUDIO,
            audio_codec=codec,
        )
    )
