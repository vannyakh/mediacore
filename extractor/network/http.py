"""Shared HTTP client helpers."""

from __future__ import annotations

import httpx

DEFAULT_HEADERS = {
    "User-Agent": "MediaCore/0.1 (+https://github.com/local/mediacore)",
    "Accept": "*/*",
}


def get_client(timeout: float = 30.0) -> httpx.Client:
    return httpx.Client(
        timeout=httpx.Timeout(timeout),
        follow_redirects=True,
        headers=DEFAULT_HEADERS,
    )
