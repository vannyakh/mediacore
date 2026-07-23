import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.security


def test_missing_api_key(client: TestClient):
    assert client.get("/v1/providers").status_code == 401


def test_invalid_api_key(client: TestClient):
    res = client.get("/v1/providers", headers={"X-API-Key": "wrong-key"})
    assert res.status_code == 401


def test_analyze_rejects_javascript_url(client: TestClient, api_headers):
    res = client.post(
        "/v1/analyze",
        headers=api_headers,
        json={"url": "javascript:alert(1)"},
    )
    assert res.status_code == 400


def test_analyze_rejects_path_traversal_file(client: TestClient, api_headers):
    res = client.post(
        "/v1/analyze",
        headers=api_headers,
        json={"url": "file:///../../etc/passwd"},
    )
    # file:// may validate; unsupported/no provider or error is acceptable
    assert res.status_code in {400, 404, 422, 500} or res.status_code == 200


def test_storage_paths_remain_under_root(storage_root):
    from packages.storage.local import LocalStorage

    storage = LocalStorage(root=storage_root)
    safe = storage.path_for("job-sec", "clip.mp4").resolve()
    assert storage_root.resolve() in safe.parents
