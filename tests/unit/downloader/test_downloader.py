from pathlib import Path

import httpx
import pytest
import respx

from packages.core.downloader import download_file, head_content_type
from packages.core.exceptions import DownloadError

pytestmark = pytest.mark.unit


@respx.mock
def test_download_file(tmp_path: Path):
    url = "https://cdn.example.com/demo.mp4"
    respx.get(url).respond(200, content=b"abc123", headers={"content-type": "video/mp4"})
    dest = tmp_path / "out.mp4"
    size, ctype = download_file(url, dest)
    assert size == 6
    assert ctype == "video/mp4"
    assert dest.read_bytes() == b"abc123"


@respx.mock
def test_download_file_http_error(tmp_path: Path):
    url = "https://cdn.example.com/missing.mp4"
    respx.get(url).respond(404)
    with pytest.raises(DownloadError):
        download_file(url, tmp_path / "out.mp4")


@respx.mock
def test_head_content_type():
    url = "https://cdn.example.com/demo.mp4"
    respx.head(url).respond(200, headers={"content-type": "video/webm"})
    assert head_content_type(url) == "video/webm"


@respx.mock
def test_head_content_type_falls_back_to_get():
    url = "https://cdn.example.com/demo.mp4"
    respx.head(url).respond(405)
    respx.get(url).respond(200, headers={"content-type": "audio/mpeg"})
    assert head_content_type(url) == "audio/mpeg"


@respx.mock
def test_head_content_type_error_returns_none():
    url = "https://cdn.example.com/demo.mp4"
    respx.head(url).mock(side_effect=httpx.ConnectError("down"))
    assert head_content_type(url) is None
