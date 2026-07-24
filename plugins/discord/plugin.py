"""Discord webhook notifications for MediaCore events."""

from __future__ import annotations

from packages.events.plugins import forward_discord, plugin_runtime_status


def _status() -> str:
    return plugin_runtime_status("mediacore-plugin-discord")


PLUGIN = {
    "name": "mediacore-plugin-discord",
    "version": "0.1.0",
    "kind": "notifications",
    "description": "Discord webhook notifications for job events",
    "status": _status(),
    "capabilities": ["events", "notify"],
}


def on_event(event) -> None:
    forward_discord(event)
