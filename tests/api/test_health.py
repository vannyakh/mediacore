import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.api


def test_health(client: TestClient):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["service"] == "mediacore-api"
