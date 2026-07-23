import pytest

pytestmark = pytest.mark.api


def test_providers_include_stubs(client, api_headers):
    res = client.get("/v1/providers", headers=api_headers)
    assert res.status_code == 200
    names = {p["name"] for p in res.json()}
    assert "youtube" in names
    assert "generic" in names
    assert len(res.json()) >= 1000


def test_catalog_summary(client, api_headers):
    res = client.get("/v1/providers/catalog", headers=api_headers)
    assert res.status_code == 200
    body = res.json()
    assert body["extractors"] >= 1000
    assert body["providers_indexed"] >= 1000


def test_catalog_search(client, api_headers):
    res = client.get("/v1/providers/catalog/search", headers=api_headers, params={"q": "tiktok"})
    assert res.status_code == 200
    assert any("tiktok" in e["ie_name"].lower() for e in res.json())
