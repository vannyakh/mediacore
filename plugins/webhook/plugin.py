"""HTTP webhook notification plugin for MediaCore events."""

from __future__ import annotations

import os

from packages.events.plugins import forward_webhook, plugin_runtime_status


def _status() -> str:
    return plugin_runtime_status("mediacore-plugin-webhook")


PLUGIN = {
    "name": "mediacore-plugin-webhook",
    "version": "0.1.0",
    "kind": "webhooks",
    "description": "Forward MediaCore events to HTTP webhooks",
    "status": _status(),
    "capabilities": ["events", "webhook"],
}


def on_event(event) -> None:
    """Called when registered as a bus listener."""
    forward_webhook(event, url=os.getenv("MEDIACORE_WEBHOOK_URL") or os.getenv("WEBHOOK_URL"))
