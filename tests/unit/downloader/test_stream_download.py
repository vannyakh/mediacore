"""Stream / HLS download routing (permitted direct playlist URLs)."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest
import respx

from packages.core.downloader import download_file, download_stream_file
from packages.core.exceptions import DownloadError
from packages.core.parser import is_stream_playlist_url
from packages.media.wrapper import FFmpegError
from providers.direct_media import direct_download, direct_metadata

pytestmark = pytest.mark.unit


def test_is_stream_playlist_url():
    assert is_stream_playlist_url("https://cdn.example.com/live/index.m3u8")
    assert is_stream_playlist_url("https://cdn.example.com/a.mpd")
    assert not is_stream_playlist_url("https://cdn.example.com/a.mp4")
    assert not is_stream_playlist_url("https://www.youtube.com/watch?v=x")


def test_download_file_routes_m3u8_to_ffmpeg(tmp_path: Path):
    dest = tmp_path / "out.mp4"
    url = "https://cdn.example.com/v/playlist.m3u8"

    def fake_stream(u: str, d: Path, *, headers=None):
        d.write_bytes(b"fake-mp4")
        return d

    with patch("packages.media.wrapper.download_stream", side_effect=fake_stream):
        size, ctype = download_file(url, dest)
    assert size == 8
    assert ctype == "video/mp4"
    assert dest.read_bytes() == b"fake-mp4"


@respx.mock
def test_download_file_routes_playlist_content_type(tmp_path: Path):
    url = "https://cdn.example.com/stream"
    respx.get(url).respond(
        200,
        content=b"#EXTM3U\n",
        headers={"content-type": "application/vnd.apple.mpegurl"},
    )
    dest = tmp_path / "out.mp4"

    def fake_stream(u: str, d: Path, *, headers=None):
        d.write_bytes(b"from-hls")
        return d

    with patch("packages.media.wrapper.download_stream", side_effect=fake_stream):
        size, _ = download_file(url, dest)
    assert size == 8
    assert dest.read_bytes() == b"from-hls"


def test_download_stream_file_requires_ffmpeg(tmp_path: Path):
    with (
        patch("packages.media.wrapper.ffmpeg_available", return_value=False),
        pytest.raises(DownloadError, match="ffmpeg"),
    ):
        download_stream_file("https://cdn.example.com/a.m3u8", tmp_path / "o.mp4")


def test_direct_media_hls_metadata_and_download(tmp_path: Path):
    url = "https://cdn.example.com/show/master.m3u8"
    with patch("providers.direct_media.head_content_type", return_value="application/vnd.apple.mpegurl"):
        meta = direct_metadata("generic", url)
    assert meta.manifest is not None
    assert meta.manifest.type == "hls"
    assert meta.formats[0].container == "mp4"

    dest = tmp_path / "clip.mp4"

    def fake_dl(u, d, **kwargs):
        d.write_bytes(b"streamed")
        return (8, "video/mp4")

    with (
        patch("providers.direct_media.head_content_type", return_value="application/vnd.apple.mpegurl"),
        patch("providers.direct_media.download_file", side_effect=fake_dl),
    ):
        result = direct_download("generic", url, "original", dest)
    assert result.filesize == 8
    assert result.container == "mp4"


def test_download_stream_raises_ffmpeg_error(tmp_path: Path):
    with (
        patch("packages.media.wrapper.ffmpeg_available", return_value=True),
        patch(
            "packages.media.wrapper.subprocess.run",
            side_effect=lambda *a, **k: type(
                "R", (), {"returncode": 1, "stderr": "bad stream", "stdout": ""}
            )(),
        ),
        pytest.raises(FFmpegError, match="bad stream"),
    ):
        from packages.media.wrapper import download_stream

        download_stream("https://cdn.example.com/a.m3u8", tmp_path / "o.mp4")
