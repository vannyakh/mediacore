import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.api


def test_providers_requires_key(client: TestClient):
    assert client.get("/v1/providers").status_code == 401


def test_providers(client: TestClient, api_headers):
    res = client.get("/v1/providers", headers=api_headers)
    assert res.status_code == 200
    names = {p["name"] for p in res.json()}
    assert "generic" in names


def test_api_v1_compat_alias(client: TestClient, api_headers):
    res = client.get("/api/v1/providers", headers=api_headers)
    assert res.status_code == 200
