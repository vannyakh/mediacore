"""Progressive HTTP media downloader (with resume + stream escalate)."""

from __future__ import annotations

from pathlib import Path

import httpx

from packages.core.downloader.progress import get_progress_callback
from packages.core.downloader.resume import existing_size, range_headers
from packages.core.downloader.stream import download_stream_file, looks_like_playlist_content_type
from packages.core.exceptions import DownloadError
from packages.core.networking import create_client, with_retries
from packages.core.networking.session import build_timeout
from packages.core.parser import is_stream_playlist_url

DEFAULT_TIMEOUT = build_timeout(connect=15.0, read=60.0, write=60.0, pool=15.0)
CHUNK_SIZE = 1024 * 64


def _write_body(
    response: httpx.Response,
    dest: Path,
    *,
    start: int,
    mode: str,
    progress,
) -> tuple[int, str | None]:
    content_type = response.headers.get("content-type")
    total_header = response.headers.get("content-length")
    content_len = int(total_header) if total_header and total_header.isdigit() else None
    if response.status_code == 206 and content_len is not None:
        total = start + content_len
    elif content_len is not None and start == 0:
        total = content_len
    else:
        total = content_len

    size = start if mode == "ab" else 0
    last_emit = -1
    if progress is not None:
        progress(size, total)
    with dest.open(mode) as fh:
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


def download_file(
    url: str,
    dest: Path,
    *,
    headers: dict[str, str] | None = None,
    timeout: httpx.Timeout | None = None,
    on_progress=None,
    allow_stream: bool = True,
    resume: bool = True,
    attempts: int = 3,
) -> tuple[int, str | None]:
    """
    Progressive HTTP download (chunked stream to disk).

    When ``allow_stream`` is true and the URL is an HLS/DASH playlist, uses ffmpeg
    to fetch the media stream (requires ffmpeg on PATH).
    When ``resume`` is true and the server returns 206, appends to a partial file.
    """
    if allow_stream and is_stream_playlist_url(url):
        return download_stream_file(url, dest, headers=headers)

    dest.parent.mkdir(parents=True, exist_ok=True)
    progress = on_progress or get_progress_callback()

    def _once() -> tuple[int, str | None]:
        start = existing_size(dest) if resume else 0
        if not resume and dest.exists():
            dest.unlink()
            start = 0
        req_headers = range_headers(start, headers)
        with create_client(timeout=timeout or DEFAULT_TIMEOUT) as client:
            with client.stream("GET", url, headers=req_headers) as response:
                if allow_stream and looks_like_playlist_content_type(
                    response.headers.get("content-type")
                ):
                    response.raise_for_status()
                    response.close()
                    return download_stream_file(url, dest, headers=headers)

                if start > 0 and response.status_code == 206:
                    return _write_body(response, dest, start=start, mode="ab", progress=progress)

                if start > 0 and response.status_code == 200:
                    # Server ignored Range — rewrite from scratch
                    dest.unlink(missing_ok=True)
                    response.raise_for_status()
                    return _write_body(response, dest, start=0, mode="wb", progress=progress)

                response.raise_for_status()
                return _write_body(response, dest, start=0, mode="wb", progress=progress)

    try:
        return with_retries(_once, attempts=attempts)
    except httpx.HTTPError as exc:
        raise DownloadError(f"Failed to download media: {exc}") from exc


def head_content_type(url: str, *, headers: dict[str, str] | None = None) -> str | None:
    try:
        with create_client(timeout=DEFAULT_TIMEOUT) as client:

            def _head() -> str | None:
                response = client.head(url, headers=headers or {})
                if response.status_code >= 400:
                    response = client.get(url, headers=headers or {})
                response.raise_for_status()
                return response.headers.get("content-type")

            return with_retries(_head, attempts=2)
    except httpx.HTTPError:
        return None
