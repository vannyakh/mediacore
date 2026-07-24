"""HTTP Range resume helpers for progressive downloads."""

from __future__ import annotations

from pathlib import Path

import httpx


def supports_resume(response: httpx.Response) -> bool:
    accept = (response.headers.get("accept-ranges") or "").lower()
    return "bytes" in accept


def existing_size(dest: Path) -> int:
    if dest.exists() and dest.is_file():
        return dest.stat().st_size
    return 0


def range_headers(start: int, base: dict[str, str] | None = None) -> dict[str, str]:
    headers = dict(base or {})
    if start > 0:
        headers["Range"] = f"bytes={start}-"
    return headers
