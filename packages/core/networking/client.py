"""Shared HTTP client helpers (yt-dlp ``networking`` counterpart)."""

from __future__ import annotations

import httpx

from packages.core.networking.defaults import DEFAULT_HEADERS
from packages.core.networking.session import create_client

__all__ = ["DEFAULT_HEADERS", "get_client"]


def get_client(timeout: float = 30.0) -> httpx.Client:
    """Return a configured client (caller should close or use as context manager)."""
    return create_client(timeout=timeout)
