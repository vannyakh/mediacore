import pytest

pytestmark = pytest.mark.security


def test_analyze_requires_api_key(client):
    res = client.post("/v1/analyze", json={"url": "https://cdn.example.com/a.mp4"})
    assert res.status_code == 401


def test_invalid_api_key(client):
    res = client.get("/v1/providers", headers={"X-API-Key": "wrong"})
    assert res.status_code == 401
