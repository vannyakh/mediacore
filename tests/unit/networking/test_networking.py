import httpx
import pytest
import respx

from packages.core.networking import create_client, get_client, merge_headers, with_retries

pytestmark = pytest.mark.unit


def test_get_client_context():
    with get_client() as client:
        assert client.headers.get("User-Agent")


def test_merge_headers_overrides():
    headers = merge_headers({"Accept": "application/json"})
    assert headers["Accept"] == "application/json"
    assert "User-Agent" in headers


@respx.mock
def test_with_retries_on_503():
    url = "https://cdn.example.com/retry"
    route = respx.get(url)
    route.side_effect = [
        httpx.Response(503),
        httpx.Response(200, json={"ok": True}),
    ]
    with create_client() as client:

        def _get():
            response = client.get(url)
            response.raise_for_status()
            return response.json()

        assert with_retries(_get, attempts=3, backoff=0) == {"ok": True}
    assert route.call_count == 2
