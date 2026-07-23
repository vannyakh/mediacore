"""Canonical plugin kinds for MediaCore."""

from __future__ import annotations

from enum import StrEnum


class PluginKind(StrEnum):
    METADATA = "metadata"
    PROVIDER = "provider"
    STORAGE = "storage"
    AUTHENTICATION = "authentication"
    AI = "ai"
    FFMPEG = "ffmpeg"
    TRANSLATION = "translation"
    NOTIFICATIONS = "notifications"
    ANALYTICS = "analytics"
    WEBHOOKS = "webhooks"


PLUGIN_STATUSES = frozenset({"available", "stub", "error", "disabled"})

# Suggested default capabilities when a plugin omits them.
DEFAULT_CAPABILITIES: dict[PluginKind, list[str]] = {
    PluginKind.METADATA: ["enrich", "normalize"],
    PluginKind.PROVIDER: ["resolve", "metadata", "download"],
    PluginKind.STORAGE: ["store", "delete", "public_url"],
    PluginKind.AUTHENTICATION: ["api_key", "verify"],
    PluginKind.AI: ["transcribe", "subtitles"],
    PluginKind.FFMPEG: ["convert", "audio", "thumbnail", "clip"],
    PluginKind.TRANSLATION: ["translate"],
    PluginKind.NOTIFICATIONS: ["events", "notify"],
    PluginKind.ANALYTICS: ["track", "metrics"],
    PluginKind.WEBHOOKS: ["events", "webhook"],
}


def parse_plugin_kind(value: str) -> PluginKind:
    try:
        return PluginKind(value)
    except ValueError as exc:
        raise ValueError(f"Unknown plugin kind: {value}") from exc
