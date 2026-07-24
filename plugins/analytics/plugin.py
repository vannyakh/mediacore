"""Job and usage analytics sink — tracks EventBus lifecycle events."""

from __future__ import annotations

from typing import Any

from packages.plugins.services import get_analytics_sink

PLUGIN = {
    "name": "mediacore-plugin-analytics",
    "version": "0.1.0",
    "kind": "analytics",
    "description": "In-process job/usage analytics sink (counts + recent events)",
    "status": "available",
    "capabilities": ["track", "metrics", "events"],
}


def create(settings: Any | None = None) -> Any:
    del settings
    return get_analytics_sink()


def on_event(event: Any) -> None:
    get_analytics_sink().on_event(event)


def metrics() -> dict[str, Any]:
    return get_analytics_sink().metrics()
