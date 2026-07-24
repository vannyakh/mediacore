"""Retry helpers for transient HTTP failures."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

import httpx

T = TypeVar("T")

RETRYABLE_STATUS = frozenset({408, 425, 429, 500, 502, 503, 504})
DEFAULT_ATTEMPTS = 3
DEFAULT_BACKOFF = 0.4


def is_retryable_status(status_code: int) -> bool:
    return status_code in RETRYABLE_STATUS


def is_retryable_exc(exc: BaseException) -> bool:
    return isinstance(
        exc,
        (
            httpx.ConnectError,
            httpx.ConnectTimeout,
            httpx.ReadTimeout,
            httpx.WriteTimeout,
            httpx.PoolTimeout,
            httpx.RemoteProtocolError,
        ),
    )


def with_retries(
    operation: Callable[[], T],
    *,
    attempts: int = DEFAULT_ATTEMPTS,
    backoff: float = DEFAULT_BACKOFF,
) -> T:
    """Run ``operation`` with capped exponential backoff on transient errors."""
    last: BaseException | None = None
    for attempt in range(max(1, attempts)):
        try:
            return operation()
        except httpx.HTTPStatusError as exc:
            last = exc
            if not is_retryable_status(exc.response.status_code) or attempt + 1 >= attempts:
                raise
        except Exception as exc:  # noqa: BLE001
            last = exc
            if not is_retryable_exc(exc) or attempt + 1 >= attempts:
                raise
        time.sleep(backoff * (2**attempt))
    assert last is not None
    raise last
