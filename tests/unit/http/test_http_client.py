import pytest

from packages.core.http import get_client

pytestmark = pytest.mark.unit


def test_http_client_context():
    with get_client() as client:
        assert client.headers.get("User-Agent")
