"""Python SDK surface (no live server)."""

from __future__ import annotations

from pathlib import Path

import httpx
import pytest

pytestmark = pytest.mark.unit

ROOT = Path(__file__).resolve().parents[3]
SDK_ROOT = ROOT / "sdk" / "python"


@pytest.fixture(scope="module")
def mediacore_sdk():
    import sys

    sys.path.insert(0, str(SDK_ROOT))
    from mediacore_sdk import MediaCore

    return MediaCore


class _Transport(httpx.BaseTransport):
    def handle_request(self, request: httpx.Request) -> httpx.Response:
        path = request.url.path
        if path == "/v1/analyze":
            body = {
                "platform": "generic",
                "title": "demo",
                "formats": [{"id": "original", "quality": "original", "container": "mp4"}],
                "url": "https://example.com/a.mp4",
            }
            return httpx.Response(200, json=body)
        if path == "/v1/download":
            return httpx.Response(
                202, json={"job_id": "j1", "status": "queued", "type": "download"}
            )
        if path == "/v1/jobs/j1":
            return httpx.Response(
                200,
                json={
                    "id": "j1",
                    "status": "completed",
                    "type": "download",
                    "url": "https://example.com/a.mp4",
                    "result_path": "/tmp/a.mp4",
                },
            )
        if path == "/v1/providers":
            return httpx.Response(200, json=[{"name": "generic", "status": "active"}])
        return httpx.Response(404, text="missing")


def test_python_sdk_analyze_download_wait(mediacore_sdk, monkeypatch: pytest.MonkeyPatch):
    transport = _Transport()
    real_client = httpx.Client

    def fake_client(*args, **kwargs):
        kwargs["transport"] = transport
        return real_client(*args, **kwargs)

    monkeypatch.setattr("mediacore_sdk.httpx.Client", fake_client)
    client = mediacore_sdk("k", base_url="http://test")
    meta = client.media.analyze("https://example.com/a.mp4")
    assert meta["platform"] == "generic"
    job = client.media.download(meta["url"])
    assert job["job_id"] == "j1"
    done = client.jobs.wait("j1", timeout=2.0, interval=0.01)
    assert done["status"] == "completed"
    assert client.providers.list()[0]["name"] == "generic"
    client.close()


def test_sdk_readme_lists_install():
    text = (ROOT / "sdk" / "README.md").read_text(encoding="utf-8")
    assert "pip install" in text
    assert "npm install" in text
    assert "composer" in text
    assert "go " in text.lower() or "go get" in text or "go mod" in text
