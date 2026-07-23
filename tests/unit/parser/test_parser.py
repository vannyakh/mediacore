import pytest

from packages.core.parser import hostname, is_direct_media_url, path_segments, query_param

pytestmark = pytest.mark.unit


def test_hostname():
    assert hostname("https://CDN.Example.com/a.mp4") == "cdn.example.com"


def test_path_segments():
    assert path_segments("https://x.com/a/b/c.mp4") == ["a", "b", "c.mp4"]


def test_query_param():
    assert query_param("https://x.com/?v=123", "v") == "123"
    assert query_param("https://x.com/", "v") is None


@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://x.com/a.mp4", True),
        ("https://x.com/a.m3u8", True),
        ("https://x.com/a.html", False),
    ],
)
def test_is_direct_media_url(url: str, expected: bool):
    assert is_direct_media_url(url) is expected
