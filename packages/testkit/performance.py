"""Lightweight performance helpers for smoke tests."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def timed_call(fn: Callable[[], T], *, iterations: int = 50) -> tuple[T | None, float]:
    """Return last result and average milliseconds per call."""
    result: T | None = None
    start = time.perf_counter()
    for _ in range(iterations):
        result = fn()
    elapsed_ms = (time.perf_counter() - start) * 1000 / iterations
    return result, elapsed_ms


def assert_latency_under(fn: Callable[[], object], *, max_ms: float, iterations: int = 50) -> float:
    _, avg_ms = timed_call(fn, iterations=iterations)
    assert avg_ms < max_ms, f"avg latency {avg_ms:.2f}ms exceeds {max_ms}ms"
    return avg_ms
