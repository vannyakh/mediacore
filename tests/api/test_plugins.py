import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.api


def test_plugins(client: TestClient, api_headers):
    res = client.get("/v1/plugins", headers=api_headers)
    assert res.status_code == 200
    assert any(p["name"].startswith("mediacore-plugin-") for p in res.json())
