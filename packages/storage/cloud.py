"""Placeholder backends for OAuth / vendor SDKs (optional; not required for local use)."""

from __future__ import annotations

from packages.core.exceptions import PluginError


def not_configured(name: str, hint: str) -> PluginError:
    return PluginError(
        f"{name} storage is optional and not configured. {hint} "
        "Local-only workflows work without this plugin — keep STORAGE_BACKEND=local."
    )
