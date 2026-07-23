import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.api


def test_system(client: TestClient, api_headers):
    res = client.get("/v1/system", headers=api_headers)
    assert res.status_code == 200
    assert res.json()["name"] == "MediaCore"
