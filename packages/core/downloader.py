"""HTTP media downloader used by providers."""

from __future__ import annotations

import threading
from collections.abc import Callable
from pathlib import Path

import httpx

from packages.core.exceptions import DownloadError

DEFAULT_TIMEOUT = httpx.Timeout(60.0, connect=15.0)
CHUNK_SIZE = 1024 * 64

ProgressCallback = Callable[[int, int | None], None]

_progress_local = threading.local()


def set_progress_callback(callback: ProgressCallback | None) -> None:
    """Thread-local progress hook used by engine during downloads."""
    _progress_local.callback = callback


def get_progress_callback() -> ProgressCallback | None:
    return getattr(_progress_local, "callback", None)


def download_file(
    url: str,
    dest: Path,
    *,
    headers: dict[str, str] | None = None,
    timeout: httpx.Timeout | None = None,
    on_progress: ProgressCallback | None = None,
) -> tuple[int, str | None]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    progress = on_progress or get_progress_callback()
    try:
        with httpx.Client(timeout=timeout or DEFAULT_TIMEOUT, follow_redirects=True) as client:
            with client.stream("GET", url, headers=headers or {}) as response:
                response.raise_for_status()
                content_type = response.headers.get("content-type")
                total_header = response.headers.get("content-length")
                total = int(total_header) if total_header and total_header.isdigit() else None
                size = 0
                last_emit = -1
                if progress is not None:
                    progress(0, total)
                with dest.open("wb") as fh:
                    for chunk in response.iter_bytes(CHUNK_SIZE):
                        fh.write(chunk)
                        size += len(chunk)
                        if progress is not None:
                            if total and total > 0:
                                percent = int(size * 100 / total)
                                if percent >= last_emit + 5 or size == total:
                                    progress(size, total)
                                    last_emit = percent
                            elif size - max(last_emit, 0) >= CHUNK_SIZE * 16:
                                progress(size, total)
                                last_emit = size
                if progress is not None:
                    progress(size, total if total is not None else size)
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
