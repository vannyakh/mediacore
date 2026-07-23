"""Python SDK for MediaCore."""

from __future__ import annotations

from typing import Any

import httpx


class MediaCore:
    def __init__(self, api_key: str, base_url: str = "http://localhost:8000") -> None:
        self._client = httpx.Client(
            base_url=base_url.rstrip("/"),
            headers={"X-API-Key": api_key},
            timeout=60.0,
        )

    @property
    def media(self) -> "_MediaAPI":
        return _MediaAPI(self._client)

    @property
    def jobs(self) -> "_JobsAPI":
        return _JobsAPI(self._client)

    @property
    def plugins(self) -> "_PluginsAPI":
        return _PluginsAPI(self._client)

    def close(self) -> None:
        self._client.close()


class _MediaAPI:
    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def analyze(self, url: str) -> dict[str, Any]:
        r = self._client.post("/v1/analyze", json={"url": url})
        r.raise_for_status()
        return r.json()

    def download(self, url: str, format_id: str = "original") -> dict[str, Any]:
        r = self._client.post("/v1/download", json={"url": url, "format": format_id})
        r.raise_for_status()
        return r.json()

    def convert(self, path: str, **options: Any) -> dict[str, Any]:
        r = self._client.post("/v1/convert", json={"path": path, "options": options})
        r.raise_for_status()
        return r.json()

    def thumbnail(self, url: str) -> dict[str, Any]:
        r = self._client.post("/v1/thumbnail", json={"url": url})
        r.raise_for_status()
        return r.json()


class _JobsAPI:
    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def get(self, job_id: str) -> dict[str, Any]:
        r = self._client.get(f"/v1/jobs/{job_id}")
        r.raise_for_status()
        return r.json()

    def list(self) -> list[dict[str, Any]]:
        return []


class _PluginsAPI:
    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def list(self) -> list[dict[str, Any]]:
        r = self._client.get("/v1/plugins")
        r.raise_for_status()
        return r.json()


# Back-compat
VideoExtractor = MediaCore
