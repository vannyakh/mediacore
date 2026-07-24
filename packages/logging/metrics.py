"""Prometheus helpers for MediaCore API."""

from __future__ import annotations

from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

REQUESTS = Counter(
    "mediacore_http_requests_total",
    "HTTP requests",
    ["method", "path", "status"],
)
LATENCY = Histogram(
    "mediacore_http_request_duration_seconds",
    "HTTP request latency",
    ["method", "path"],
)


def observe_request(method: str, path: str, status: int, duration: float) -> None:
    REQUESTS.labels(method=method, path=path, status=str(status)).inc()
    LATENCY.labels(method=method, path=path).observe(duration)


def render_metrics() -> tuple[bytes, str]:
    return generate_latest(), CONTENT_TYPE_LATEST
