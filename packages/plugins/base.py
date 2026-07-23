"""Plugin protocol — manifests plus optional runtime factories."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class Plugin(Protocol):
    """Optional richer plugin module surface beyond a PLUGIN dict."""

    PLUGIN: dict[str, Any]

    def create(self, settings: Any | None = None) -> Any:
        """Return a runtime handler for this plugin (optional)."""
        ...

    def on_event(self, event: Any) -> None:
        """Handle a MediaCore event (notifications / webhooks)."""
        ...
