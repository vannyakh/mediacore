"""Telegram Bot API notifications for MediaCore events."""

from __future__ import annotations

from packages.events.plugins import forward_telegram, plugin_runtime_status


def _status() -> str:
    return plugin_runtime_status("mediacore-plugin-telegram")


PLUGIN = {
    "name": "mediacore-plugin-telegram",
    "version": "0.1.0",
    "kind": "notifications",
    "description": "Telegram bot notifications for job events",
    "status": _status(),
    "capabilities": ["events", "notify"],
}


def on_event(event) -> None:
    forward_telegram(event)
