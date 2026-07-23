import pytest
from fastapi.testclient import TestClient

from packages.core.models import FormatInfo, MediaMetadata

pytestmark = pytest.mark.api


def test_download_creates_job(client: TestClient, api_headers, monkeypatch):
    def fake_analyze(self, url, allow_private=False):
        return MediaMetadata(
            platform="generic",
            url=url,
            title="demo.mp4",
            formats=[FormatInfo(id="original", quality="original", container="mp4")],
        )

    monkeypatch.setattr("packages.engine.engine.MediaCoreEngine.analyze", fake_analyze)
    monkeypatch.setattr("apps.api.routes.v1.enqueue_download", lambda job_id: None)

    res = client.post(
        "/v1/download",
        headers=api_headers,
        json={"url": "https://cdn.example.com/demo.mp4", "format": "original"},
    )
    assert res.status_code == 202
    body = res.json()
    assert body["job_id"]
    assert body["type"] == "download"

    job = client.get(f"/v1/jobs/{body['job_id']}", headers=api_headers)
    assert job.status_code == 200
    assert job.json()["id"] == body["job_id"]


def test_job_not_found(client: TestClient, api_headers):
    res = client.get("/v1/jobs/does-not-exist", headers=api_headers)
    assert res.status_code == 404


def test_list_jobs(client: TestClient, api_headers, monkeypatch):
    def fake_analyze(self, url, allow_private=False):
        return MediaMetadata(
            platform="generic",
            url=url,
            title="demo.mp4",
            formats=[FormatInfo(id="original", quality="original", container="mp4")],
        )

    monkeypatch.setattr("packages.engine.engine.MediaCoreEngine.analyze", fake_analyze)
    monkeypatch.setattr("apps.api.routes.v1.enqueue_download", lambda job_id: None)

    created = client.post(
        "/v1/download",
        headers=api_headers,
        json={"url": "https://cdn.example.com/demo.mp4", "format": "original"},
    )
    assert created.status_code == 202

    res = client.get("/v1/jobs", headers=api_headers)
    assert res.status_code == 200
    jobs = res.json()
    assert isinstance(jobs, list)
    assert any(j["id"] == created.json()["job_id"] for j in jobs)
