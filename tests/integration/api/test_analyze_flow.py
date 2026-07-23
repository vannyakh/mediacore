import pytest
from fastapi.testclient import TestClient

from packages.core.models import FormatInfo, MediaMetadata

pytestmark = pytest.mark.integration


def test_analyze_to_job_pipeline(client: TestClient, api_headers, monkeypatch):
    def fake_analyze(self, url, allow_private=False):
        return MediaMetadata(
            platform="generic",
            url=url,
            title="demo.mp4",
            formats=[FormatInfo(id="original", quality="original", container="mp4")],
            manifest={"type": "direct"},
        )

    monkeypatch.setattr("packages.engine.engine.MediaCoreEngine.analyze", fake_analyze)
    monkeypatch.setattr("apps.api.routes.v1.enqueue_download", lambda job_id: None)

    analyze = client.post(
        "/v1/analyze",
        headers=api_headers,
        json={"url": "https://cdn.example.com/demo.mp4"},
    )
    assert analyze.status_code == 200
    assert analyze.json()["platform"] == "generic"

    download = client.post(
        "/v1/download",
        headers=api_headers,
        json={"url": "https://cdn.example.com/demo.mp4", "format": "original"},
    )
    assert download.status_code == 202
    job_id = download.json()["job_id"]

    job = client.get(f"/v1/jobs/{job_id}", headers=api_headers)
    assert job.status_code == 200
    assert job.json()["url"] == "https://cdn.example.com/demo.mp4"
