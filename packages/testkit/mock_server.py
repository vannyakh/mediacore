"""Minimal ASGI-style mock HTTP server helpers for E2E tests."""

from __future__ import annotations

from dataclasses import dataclass

import httpx


@dataclass
class MockMediaResponse:
    path: str = "/media/demo.mp4"
    body: bytes = b"mock-media-content"
    content_type: str = "video/mp4"


def make_mock_transport(response: MockMediaResponse | None = None) -> httpx.MockTransport:
    media = response or MockMediaResponse()

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == media.path or str(request.url).endswith(media.path):
            return httpx.Response(
                200,
                content=media.body,
                headers={"content-type": media.content_type},
            )
        if request.method == "HEAD":
            return httpx.Response(200, headers={"content-type": media.content_type})
        return httpx.Response(404, text="not found")

    return httpx.MockTransport(handler)
