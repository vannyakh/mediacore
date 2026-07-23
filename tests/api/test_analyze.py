import pytest
from fastapi.testclient import TestClient

from packages.core.models import FormatInfo, MediaMetadata

pytestmark = pytest.mark.api


def test_analyze_generic(client: TestClient, api_headers, monkeypatch):
    def fake_analyze(self, url, allow_private=False):
        return MediaMetadata(
            platform="generic",
            url=url,
            title="demo.mp4",
            formats=[FormatInfo(id="original", quality="original", container="mp4")],
            manifest={"type": "direct"},
        )

    monkeypatch.setattr("packages.engine.engine.MediaCoreEngine.analyze", fake_analyze)
    res = client.post(
        "/v1/analyze",
        headers=api_headers,
        json={"url": "https://cdn.example.com/demo.mp4"},
    )
    assert res.status_code == 200
    body = res.json()
    assert body["platform"] == "generic"
    assert body["formats"][0]["id"] == "original"


def test_analyze_invalid_url(client: TestClient, api_headers):
    res = client.post(
        "/v1/analyze",
        headers=api_headers,
        json={"url": "ftp://bad.example/a.mp4"},
    )
    assert res.status_code == 400
