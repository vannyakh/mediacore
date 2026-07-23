from pathlib import Path
from unittest.mock import patch

import pytest

from packages.testkit.contracts import run_provider_contract
from providers.example.provider import ExampleProvider
from providers.filesystem.provider import FilesystemProvider
from providers.generic.provider import GenericHTTPProvider
from providers.vimeo.provider import VimeoProvider

pytestmark = pytest.mark.provider


def test_generic_contract(tmp_path: Path):
    provider = GenericHTTPProvider()
    url = "https://cdn.example.com/demo.mp4"
    with (
        patch("providers.generic.provider.head_content_type", return_value="video/mp4"),
        patch("providers.generic.provider.download_file", return_value=(4, "video/mp4")),
    ):
        run_provider_contract(provider, url, tmp_path / "out.mp4", expect_download=True)


def test_filesystem_contract(tmp_path: Path):
    src = tmp_path / "local.mp4"
    src.write_bytes(b"local-bytes")
    provider = FilesystemProvider()
    run_provider_contract(provider, src.as_uri(), tmp_path / "copied.mp4", expect_download=True)


def test_example_contract_metadata_only(tmp_path: Path):
    provider = ExampleProvider()
    run_provider_contract(
        provider,
        "mediacore://example/demo",
        tmp_path / "out.mp4",
        expect_download=False,
    )


def test_vimeo_contract_metadata_only(tmp_path: Path):
    provider = VimeoProvider()
    fake = {
        "title": "Public Clip",
        "duration": 10,
        "thumbnail_url": "https://i.vimeocdn.com/t.jpg",
        "author_name": "Author",
        "provider_url": "https://vimeo.com/",
        "html": "<iframe></iframe>",
    }
    with patch("providers.vimeo.provider.httpx.Client") as client_cls:
        client = client_cls.return_value.__enter__.return_value
        response = client.get.return_value
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = fake
        run_provider_contract(
            provider,
            "https://vimeo.com/123456789",
            tmp_path / "out.mp4",
            expect_download=False,
        )
