"""Shared HTTP client helpers for the MediaCore CLI."""

from __future__ import annotations

import json
import os
import sys
from typing import Any

import httpx

DEFAULT_BASE = "http://localhost:8000"
DEFAULT_KEY = "dev-api-key-change-me"
TERMINAL_JOB_STATUSES = frozenset({"completed", "failed", "cancelled", "expired"})


def resolve_base(cli_value: str | None = None) -> str:
    return (cli_value or os.environ.get("MEDIACORE_BASE") or DEFAULT_BASE).rstrip("/")


def resolve_key(cli_value: str | None = None) -> str:
    return cli_value or os.environ.get("MEDIACORE_API_KEY") or DEFAULT_KEY


def make_client(base: str, key: str, timeout: float = 60.0) -> httpx.Client:
    return httpx.Client(
        base_url=base.rstrip("/"),
        headers={"X-API-Key": key, "Content-Type": "application/json"},
        timeout=timeout,
    )


def print_json(data: Any) -> None:
    print(json.dumps(data, indent=2, default=str))


_NOT_CONFIGURED_HINT = (
    "Page/watch URLs need a permitted API; direct media on known hosts may still download. "
    "See: mediacore providers list"
)


def format_http_error(exc: Exception) -> str:
    if isinstance(exc, httpx.HTTPStatusError):
        res = exc.response
        detail: Any
        try:
            detail = res.json()
        except Exception:  # noqa: BLE001
            detail = res.text
        message = f"HTTP {res.status_code}: {detail}"
        code = None
        if isinstance(detail, dict):
            nested = detail.get("detail")
            if isinstance(nested, dict):
                code = nested.get("code")
            else:
                code = detail.get("code")
        if code == "provider_not_configured":
            message = f"{message}\nhint: {_NOT_CONFIGURED_HINT}"
        return message
    if isinstance(exc, httpx.RequestError):
        return f"request failed: {exc}"
    return str(exc)


def request_json(
    client: httpx.Client,
    method: str,
    path: str,
    *,
    json_body: dict[str, Any] | None = None,
    params: dict[str, Any] | None = None,
) -> Any:
    res = client.request(method, path, json=json_body, params=params)
    res.raise_for_status()
    if res.status_code == 204 or not res.content:
        return None
    return res.json()


def wait_for_job(
    client: httpx.Client,
    job_id: str,
    *,
    timeout: float = 120.0,
    interval: float = 0.5,
) -> dict[str, Any]:
    import time

    deadline = time.monotonic() + timeout
    last: dict[str, Any] | None = None
    while time.monotonic() < deadline:
        last = request_json(client, "GET", f"/v1/jobs/{job_id}")
        status = str(last.get("status", ""))
        if status in TERMINAL_JOB_STATUSES:
            return last
        time.sleep(interval)
    raise TimeoutError(f"job {job_id} did not finish within {timeout:.0f}s (last={last})")


def eprint(message: str) -> None:
    print(message, file=sys.stderr)
