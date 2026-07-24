"""Optional event notification helpers (env-configured; no plugin packages required)."""

from __future__ import annotations

import logging
import os

import httpx

from packages.events.bus import Event, EventBus

logger = logging.getLogger("mediacore.events.plugins")


def _settings_value(*names: str) -> str | None:
    try:
        from packages.config.settings import get_settings

        settings = get_settings()
        mapping = {
            "MEDIACORE_WEBHOOK_URL": getattr(settings, "webhook_url", None),
            "WEBHOOK_URL": getattr(settings, "webhook_url", None),
        }
    except Exception:  # noqa: BLE001
        mapping = {}
    for name in names:
        value = os.getenv(name) or mapping.get(name)
        if value:
            return value
    return None


def _webhook_url() -> str | None:
    return _settings_value("MEDIACORE_WEBHOOK_URL", "WEBHOOK_URL")


def forward_webhook(event: Event, *, url: str | None = None) -> None:
    target = url or _webhook_url()
    if not target:
        return
    try:
        with httpx.Client(timeout=10.0) as client:
            client.post(target, json=event.to_dict())
    except Exception:  # noqa: BLE001
        logger.exception("Webhook forward failed for %s", event.type.value)


def register_event_plugins(bus: EventBus) -> list[str]:
    """Register optional in-process webhook forwarder when configured."""
    enabled: list[str] = []
    if _webhook_url():
        bus.on(None, forward_webhook)
        enabled.append("webhook")
        logger.info("Webhook event forwarder ready")
    return enabled


def plugin_runtime_status(name: str) -> str:
    """Compatibility helper for callers that still query notification status."""
    if name in {"mediacore-plugin-webhook", "webhook"}:
        return "available" if _webhook_url() else "stub"
    return "stub"
