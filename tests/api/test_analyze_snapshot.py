import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from packages.core.models import FormatInfo, MediaMetadata

pytestmark = pytest.mark.api


SNAPSHOT = Path(__file__).resolve().parents[1] / "snapshots" / "analyze_generic.json"


def test_analyze_metadata_snapshot(client: TestClient, api_headers, monkeypatch):
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
    expected = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    assert body["platform"] == expected["platform"]
    assert body["title"] == expected["title"]
    assert body["formats"][0]["id"] == expected["formats"][0]["id"]
    assert body["manifest"]["type"] == expected["manifest"]["type"]
