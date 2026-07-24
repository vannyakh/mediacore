"""Whisper transcription — optional AI plugin (stub until model runtime is wired)."""

from __future__ import annotations

from typing import Any

from packages.core.exceptions import PluginError

PLUGIN = {
    "name": "mediacore-plugin-whisper",
    "version": "0.1.0",
    "kind": "ai",
    "description": "Speech-to-text / subtitles via Whisper (optional heavy dependency)",
    "status": "stub",
    "capabilities": ["transcribe", "subtitles"],
}


def create(settings: Any | None = None) -> Any:
    del settings
    raise PluginError(
        "Whisper plugin is not configured. "
        "Install a Whisper runtime and set WHISPER_MODEL when enabling this plugin."
    )
