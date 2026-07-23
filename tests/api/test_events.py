import json

import pytest
from fastapi.testclient import TestClient

from packages.core.models import FormatInfo, MediaMetadata
from packages.events.bus import EventType, get_event_bus

pytestmark = pytest.mark.api


def test_list_events_and_cancel(client: TestClient, api_headers, monkeypatch):
    def fake_analyze(self, url, allow_private=False, job_id=None):
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
    job_id = created.json()["job_id"]

    hist = client.get("/v1/events", headers=api_headers)
    assert hist.status_code == 200
    body = hist.json()
    assert body["count"] >= 1
    types = {e["type"] for e in body["events"]}
    assert "JobCreated" in types

    filtered = client.get(f"/v1/events?job_id={job_id}", headers=api_headers)
    assert filtered.status_code == 200
    assert all(e["payload"].get("job_id") == job_id for e in filtered.json()["events"])

    cancelled = client.post(f"/v1/jobs/{job_id}/cancel", headers=api_headers)
    assert cancelled.status_code == 200
    assert cancelled.json()["status"] == "cancelled"

    again = client.post(f"/v1/jobs/{job_id}/cancel", headers=api_headers)
    assert again.status_code == 409

    events = client.get(f"/v1/events?job_id={job_id}", headers=api_headers).json()["events"]
    assert any(e["type"] == "Cancelled" for e in events)


def test_events_stream_replays_history(client: TestClient, api_headers):
    bus = get_event_bus()
    bus.emit(EventType.PROGRESS, job_id="stream-1", percent=5)

    with client.stream(
        "GET", "/v1/events/stream?replay_only=true", headers=api_headers
    ) as response:
        assert response.status_code == 200
        assert "text/event-stream" in response.headers["content-type"]
        found = False
        for line in response.iter_lines():
            if line.startswith("data:"):
                payload = json.loads(line.split(":", 1)[1].strip())
                if payload.get("type") == "Progress":
                    found = True
                    break
        assert found
