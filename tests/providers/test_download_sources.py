"""Platform download-source checks — active providers fetch; metadata_only does not."""

from __future__ import annotations

import threading
from contextlib import ExitStack
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

import pytest

from packages.core.exceptions import ProviderNotConfiguredError
from packages.engine.engine import MediaCoreEngine
from packages.registry.providers import reset_registry

pytestmark = pytest.mark.provider

# (platform, sample_url, patch targets that replace network I/O)
_DOWNLOAD_CASES: list[tuple[str, str, list[str]]] = [
    (
        "generic",
        "https://cdn.example.com/clip.mp4",
        [
            "providers.direct_media.head_content_type",
            "providers.direct_media.download_file",
        ],
    ),
    (
        "dropbox",
        "https://www.dropbox.com/s/abc123/demo.mp4?dl=0",
        [
            "providers.dropbox.provider.head_content_type",
            "providers.dropbox.provider.download_file",
        ],
    ),
    (
        "google_drive",
        "https://drive.google.com/file/d/1AbCDefGhIjK/view?usp=sharing",
        [
            "providers.google_drive.provider.head_content_type",
            "providers.google_drive.provider.download_file",
        ],
    ),
    (
        "media.ccc.de",
        "https://media.ccc.de/v/camp2023-demo",
        [
            "providers.media_ccc_de.provider.httpx.Client",
            "providers.media_ccc_de.provider.download_file",
        ],
    ),
]

_METADATA_ONLY_URLS: list[tuple[str, str]] = [
    ("youtube", "https://www.youtube.com/watch?v=jNQXAC9IVRw"),
    ("tiktok", "https://www.tiktok.com/@scout2015/video/6718335390845095173"),
    ("vimeo", "https://vimeo.com/148751763"),
]


def _patch_download_io(targets: list[str]) -> ExitStack:
    """Stack patches so metadata HEAD + download do not hit the network."""
    stack = ExitStack()
    for target in targets:
        if target.endswith("httpx.Client"):
            client_cls = stack.enter_context(patch(target))
            client = client_cls.return_value.__enter__.return_value
            response = client.get.return_value
            response.status_code = 200
            response.raise_for_status.return_value = None
            response.json.return_value = {
                "title": "Demo talk",
                "description": "Desc",
                "length": 60,
                "thumb_url": "https://static.media.ccc.de/t.jpg",
                "persons": ["Speaker"],
                "guid": "abc",
                "slug": "camp2023-demo",
                "recordings": [
                    {
                        "recording_url": "https://cdn.example.com/demo.mp4",
                        "folder": "h264-hd",
                        "language": "eng",
                        "mime_type": "video/mp4",
                        "height": 720,
                        "width": 1280,
                    }
                ],
            }
        elif target.endswith("head_content_type"):
            stack.enter_context(patch(target, return_value="video/mp4"))
        elif target.endswith("download_file"):
            stack.enter_context(patch(target, return_value=(16, "video/mp4")))
        else:
            stack.enter_context(patch(target))
    return stack


@pytest.fixture
def engine() -> MediaCoreEngine:
    return MediaCoreEngine(registry=reset_registry())


@pytest.mark.parametrize("platform,url,patches", _DOWNLOAD_CASES, ids=[c[0] for c in _DOWNLOAD_CASES])
def test_active_platform_download_via_engine(
    engine: MediaCoreEngine,
    tmp_path: Path,
    platform: str,
    url: str,
    patches: list[str],
):
    provider = engine.registry.resolve(url)
    assert provider.name == platform
    assert getattr(provider, "status", None) == "active"
    assert "download" in provider.capabilities.to_list()

    dest = tmp_path / f"{platform}.mp4"
    with _patch_download_io(patches):
        meta = engine.analyze(url)
        assert meta.platform == platform
        assert meta.formats
        result = engine.download(url, meta.formats[0].id, dest)
    assert result.format_id
    assert result.path == dest or dest.exists() or result.filesize is not None


def test_filesystem_platform_download_via_engine(engine: MediaCoreEngine, tmp_path: Path):
    src = tmp_path / "local-source.mp4"
    src.write_bytes(b"mediacore-local-bytes")
    url = src.as_uri()
    provider = engine.registry.resolve(url)
    assert provider.name == "filesystem"
    assert provider.status == "active"

    dest = tmp_path / "copied.mp4"
    meta = engine.analyze(url, allow_private=True)
    result = engine.download(url, meta.formats[0].id, dest, allow_private=True)
    assert dest.exists()
    assert dest.read_bytes() == b"mediacore-local-bytes"
    assert result.path == dest


@pytest.mark.parametrize("platform,url", _METADATA_ONLY_URLS, ids=[c[0] for c in _METADATA_ONLY_URLS])
def test_metadata_only_platform_refuses_download(
    engine: MediaCoreEngine,
    tmp_path: Path,
    platform: str,
    url: str,
):
    provider = engine.registry.resolve(url)
    assert provider.name == platform
    assert provider.status == "metadata_only"

    with patch("providers.oembed.httpx.Client") as client_cls:
        client = client_cls.return_value.__enter__.return_value
        response = client.get.return_value
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = {
            "title": "Preview",
            "author_name": "Author",
            "thumbnail_url": "https://example.com/t.jpg",
            "html": "<iframe></iframe>",
            "type": "video",
        }
        meta = engine.analyze(url)
        assert meta.platform == platform
        with pytest.raises(ProviderNotConfiguredError):
            engine.download(url, meta.formats[0].id, tmp_path / "out.mp4")


def test_download_capable_registry_names(engine: MediaCoreEngine):
    """Working download providers must register as active with download capability."""
    expected = {"filesystem", "generic", "dropbox", "google_drive", "media.ccc.de"}
    found = {
        row["name"]
        for row in engine.providers()
        if row.get("status") == "active" and "download" in (row.get("capabilities") or [])
    }
    assert expected.issubset(found)


def test_live_generic_http_download_from_local_server(tmp_path: Path):
    """Real HTTP fetch through generic → core downloader (local server, allow_private)."""
    media = tmp_path / "sample.mp4"
    payload = b"\x00\x00\x00\x18ftypmp42mediacore-test"
    media.write_bytes(payload)
    root = str(tmp_path)

    class _Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=root, **kwargs)

        def log_message(self, format: str, *args) -> None:  # noqa: A003
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address
        url = f"http://{host}:{port}/sample.mp4"
        engine = MediaCoreEngine(registry=reset_registry())
        provider = engine.registry.resolve(url)
        assert provider.name == "generic"

        dest = tmp_path / "downloaded.mp4"
        meta = engine.analyze(url, allow_private=True)
        assert meta.platform == "generic"
        result = engine.download(url, meta.formats[0].id, dest, allow_private=True)
        assert dest.exists()
        assert dest.read_bytes() == payload
        assert result.path == dest
    finally:
        server.shutdown()
        server.server_close()
