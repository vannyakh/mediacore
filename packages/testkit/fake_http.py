"""httpx mock helpers for provider/downloader tests."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

import httpx
import respx


@contextmanager
def mock_media_url(
    url: str,
    *,
    body: bytes = b"\x00\x00fake",
    content_type: str = "video/mp4",
    status_code: int = 200,
) -> Iterator[respx.MockRouter]:
    with respx.mock(assert_all_called=False) as router:
        router.head(url).respond(status_code, headers={"content-type": content_type})
        router.get(url).respond(status_code, content=body, headers={"content-type": content_type})
        yield router


def httpx_mock_transport(handler: Any) -> httpx.MockTransport:
    return httpx.MockTransport(handler)
