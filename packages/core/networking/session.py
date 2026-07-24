"""Shared HTTP session factory (timeouts, headers, proxy, cookies)."""

from __future__ import annotations

from typing import Any

import httpx

from packages.core.networking.defaults import DEFAULT_HEADERS

DEFAULT_CONNECT = 15.0
DEFAULT_READ = 60.0
DEFAULT_WRITE = 60.0
DEFAULT_POOL = 15.0
DEFAULT_MAX_REDIRECTS = 20


def build_timeout(
    *,
    connect: float = DEFAULT_CONNECT,
    read: float = DEFAULT_READ,
    write: float = DEFAULT_WRITE,
    pool: float = DEFAULT_POOL,
    total: float | None = None,
) -> httpx.Timeout:
    if total is not None:
        return httpx.Timeout(total)
    return httpx.Timeout(connect=connect, read=read, write=write, pool=pool)


def merge_headers(
    extra: dict[str, str] | None = None,
    *,
    base: dict[str, str] | None = None,
) -> dict[str, str]:
    headers = dict(base or DEFAULT_HEADERS)
    if extra:
        headers.update(extra)
    return headers


def create_client(
    *,
    timeout: httpx.Timeout | float | None = None,
    headers: dict[str, str] | None = None,
    cookies: httpx.Cookies | dict[str, str] | None = None,
    proxy: str | None = None,
    max_redirects: int = DEFAULT_MAX_REDIRECTS,
    follow_redirects: bool = True,
) -> httpx.Client:
    """Create an httpx client with MediaCore defaults."""
    kwargs: dict[str, Any] = {
        "timeout": timeout if isinstance(timeout, httpx.Timeout) else build_timeout(total=timeout),
        "follow_redirects": follow_redirects,
        "headers": merge_headers(headers),
        "max_redirects": max_redirects,
    }
    if cookies is not None:
        kwargs["cookies"] = cookies
    if proxy:
        kwargs["proxy"] = proxy
    return httpx.Client(**kwargs)
