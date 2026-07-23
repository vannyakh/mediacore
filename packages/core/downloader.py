"""HTTP media downloader used by providers."""

from __future__ import annotations

from pathlib import Path

import httpx

from packages.core.exceptions import DownloadError

DEFAULT_TIMEOUT = httpx.Timeout(60.0, connect=15.0)
CHUNK_SIZE = 1024 * 64


def download_file(
    url: str,
    dest: Path,
    *,
    headers: dict[str, str] | None = None,
    timeout: httpx.Timeout | None = None,
) -> tuple[int, str | None]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        with httpx.Client(timeout=timeout or DEFAULT_TIMEOUT, follow_redirects=True) as client:
            with client.stream("GET", url, headers=headers or {}) as response:
                response.raise_for_status()
                content_type = response.headers.get("content-type")
                size = 0
                with dest.open("wb") as fh:
                    for chunk in response.iter_bytes(CHUNK_SIZE):
                        fh.write(chunk)
                        size += len(chunk)
                return size, content_type
    except httpx.HTTPError as exc:
        raise DownloadError(f"Failed to download media: {exc}") from exc


def head_content_type(url: str, *, headers: dict[str, str] | None = None) -> str | None:
    try:
        with httpx.Client(timeout=DEFAULT_TIMEOUT, follow_redirects=True) as client:
            response = client.head(url, headers=headers or {})
            if response.status_code >= 400:
                response = client.get(url, headers=headers or {})
            response.raise_for_status()
            return response.headers.get("content-type")
    except httpx.HTTPError:
        return None
