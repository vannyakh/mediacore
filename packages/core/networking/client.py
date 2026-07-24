"""Shared HTTP client helpers (yt-dlp ``networking`` counterpart)."""

from __future__ import annotations

import httpx

DEFAULT_HEADERS = {
    "User-Agent": "MediaCore/0.1 (+https://github.com/mediacore/mediacore)",
    "Accept": "*/*",
}


def get_client(timeout: float = 30.0) -> httpx.Client:
    return httpx.Client(
        timeout=httpx.Timeout(timeout),
        follow_redirects=True,
        headers=DEFAULT_HEADERS,
    )
