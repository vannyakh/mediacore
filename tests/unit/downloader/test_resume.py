from pathlib import Path

import pytest
import respx

from packages.core.downloader import download_file

pytestmark = pytest.mark.unit


@respx.mock
def test_download_resume_appends(tmp_path: Path):
    url = "https://cdn.example.com/partial.mp4"
    dest = tmp_path / "out.mp4"
    dest.write_bytes(b"abc")

    respx.get(url).respond(
        206,
        content=b"def",
        headers={
            "content-type": "video/mp4",
            "content-length": "3",
            "accept-ranges": "bytes",
            "content-range": "bytes 3-5/6",
        },
    )
    size, ctype = download_file(url, dest, resume=True, attempts=1)
    assert size == 6
    assert ctype == "video/mp4"
    assert dest.read_bytes() == b"abcdef"
