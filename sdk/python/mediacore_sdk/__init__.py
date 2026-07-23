"""Python SDK for MediaCore — unified client surface."""

from __future__ import annotations

from typing import Any

import httpx


class MediaCore:
    """
    client.media.analyze / download / convert / thumbnail
    client.jobs.list / get
    client.plugins.list
    """

    def __init__(self, api_key: str, base_url: str = "http://localhost:8000") -> None:
        self._client = httpx.Client(
            base_url=base_url.rstrip("/"),
            headers={"X-API-Key": api_key, "Content-Type": "application/json"},
            timeout=60.0,
        )
        self.media = _MediaAPI(self._client)
        self.jobs = _JobsAPI(self._client)
        self.plugins = _PluginsAPI(self._client)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> MediaCore:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


class _MediaAPI:
    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def analyze(self, url: str) -> dict[str, Any]:
        r = self._client.post("/v1/analyze", json={"url": url})
        r.raise_for_status()
        return r.json()

    def download(self, url: str, format: str = "original") -> dict[str, Any]:
        r = self._client.post("/v1/download", json={"url": url, "format": format})
        r.raise_for_status()
        return r.json()

    def convert(self, path: str, **options: Any) -> dict[str, Any]:
        r = self._client.post("/v1/convert", json={"path": path, "options": options})
        r.raise_for_status()
        return r.json()

    def thumbnail(self, url: str, **options: Any) -> dict[str, Any]:
        body: dict[str, Any] = {"url": url}
        if options:
            body["options"] = options
        r = self._client.post("/v1/thumbnail", json=body)
        r.raise_for_status()
        return r.json()


class _JobsAPI:
    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def list(self, limit: int = 50) -> list[dict[str, Any]]:
        r = self._client.get("/v1/jobs", params={"limit": limit})
        r.raise_for_status()
        return r.json()

    def get(self, job_id: str) -> dict[str, Any]:
        r = self._client.get(f"/v1/jobs/{job_id}")
        r.raise_for_status()
        return r.json()


class _PluginsAPI:
    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def list(self) -> list[dict[str, Any]]:
        r = self._client.get("/v1/plugins")
        r.raise_for_status()
        return r.json()


__all__ = ["MediaCore"]
