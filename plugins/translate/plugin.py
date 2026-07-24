"""Translation plugin — stub until a provider (official API) is selected."""

from __future__ import annotations

from typing import Any

from packages.core.exceptions import PluginError

PLUGIN = {
    "name": "mediacore-plugin-translate",
    "version": "0.1.0",
    "kind": "translation",
    "description": "Subtitle/text translation (configure an official translation API)",
    "status": "stub",
    "capabilities": ["translate"],
}


def create(settings: Any | None = None) -> Any:
    del settings
    raise PluginError(
        "Translate plugin is not configured. "
        "Wire an official translation API and set TRANSLATE_API_KEY."
    )
