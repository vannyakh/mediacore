"""Notification helpers + plugin status. Delivery is via PluginRuntime.dispatch_event."""

from __future__ import annotations

import logging
import os
from typing import Any

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
            "MEDIACORE_TELEGRAM_BOT_TOKEN": getattr(settings, "telegram_bot_token", None),
            "TELEGRAM_BOT_TOKEN": getattr(settings, "telegram_bot_token", None),
            "MEDIACORE_TELEGRAM_CHAT_ID": getattr(settings, "telegram_chat_id", None),
            "TELEGRAM_CHAT_ID": getattr(settings, "telegram_chat_id", None),
            "MEDIACORE_DISCORD_WEBHOOK_URL": getattr(settings, "discord_webhook_url", None),
            "DISCORD_WEBHOOK_URL": getattr(settings, "discord_webhook_url", None),
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


def _telegram_config() -> tuple[str, str] | None:
    token = _settings_value("MEDIACORE_TELEGRAM_BOT_TOKEN", "TELEGRAM_BOT_TOKEN")
    chat_id = _settings_value("MEDIACORE_TELEGRAM_CHAT_ID", "TELEGRAM_CHAT_ID")
    if token and chat_id:
        return token, chat_id
    return None


def _discord_url() -> str | None:
    return _settings_value("MEDIACORE_DISCORD_WEBHOOK_URL", "DISCORD_WEBHOOK_URL")


def forward_webhook(event: Event, *, url: str | None = None) -> None:
    target = url or _webhook_url()
    if not target:
        return
    try:
        with httpx.Client(timeout=10.0) as client:
            client.post(target, json=event.to_dict())
    except Exception:  # noqa: BLE001
        logger.exception("Webhook forward failed for %s", event.type.value)


def forward_telegram(event: Event) -> None:
    cfg = _telegram_config()
    if cfg is None:
        return
    token, chat_id = cfg
    text = f"MediaCore {event.type.value}: {event.payload}"
    try:
        with httpx.Client(timeout=10.0) as client:
            client.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                json={"chat_id": chat_id, "text": text[:4000]},
            )
    except Exception:  # noqa: BLE001
        logger.exception("Telegram notify failed for %s", event.type.value)


def forward_discord(event: Event) -> None:
    url = _discord_url()
    if not url:
        return
    content = f"**MediaCore** `{event.type.value}`\n```{event.payload}```"
    try:
        with httpx.Client(timeout=10.0) as client:
            client.post(url, json={"content": content[:1900]})
    except Exception:  # noqa: BLE001
        logger.exception("Discord notify failed for %s", event.type.value)


def register_event_plugins(bus: EventBus) -> list[str]:
    """Log which notification plugins are configured.

    Delivery runs through ``PluginRuntime.dispatch_event`` → each plugin's
    ``on_event`` (no duplicate bus listeners — avoids double webhook sends).
    """
    del bus  # API lifespan still calls this for startup logging
    enabled: list[str] = []
    if _webhook_url():
        enabled.append("mediacore-plugin-webhook")
        logger.info("Webhook plugin ready (on_event)")
    if _telegram_config():
        enabled.append("mediacore-plugin-telegram")
        logger.info("Telegram plugin ready (on_event)")
    if _discord_url():
        enabled.append("mediacore-plugin-discord")
        logger.info("Discord plugin ready (on_event)")
    return enabled


def plugin_runtime_status(name: str) -> str:
    """Dynamic status for notification plugins based on env credentials."""
    if name == "mediacore-plugin-webhook":
        return "available" if _webhook_url() else "stub"
    if name == "mediacore-plugin-telegram":
        return "available" if _telegram_config() else "stub"
    if name == "mediacore-plugin-discord":
        return "available" if _discord_url() else "stub"
    return "stub"
