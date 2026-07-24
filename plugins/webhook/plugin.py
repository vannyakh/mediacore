"""HTTP webhook notification plugin for MediaCore events."""

from __future__ import annotations

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
    """Invoked by PluginRuntime.dispatch_event on every bus emit."""
    forward_webhook(event)
