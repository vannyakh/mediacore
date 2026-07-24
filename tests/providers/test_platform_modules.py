"""Platform modules: direct-media download vs page URL not_configured."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from packages.core.exceptions import ProviderNotConfiguredError
from packages.registry.providers import reset_registry
from providers.base_module import PlatformModule
from providers.platforms.factory import build_platform_modules

pytestmark = pytest.mark.provider


def test_modules_dir_exists_stubs_gone():
    root = Path(__file__).resolve().parents[2] / "providers"
    assert (root / "modules").is_dir()
    assert not (root / "stubs").exists()


def test_platform_module_direct_media_metadata_and_download(tmp_path: Path):
    mod = PlatformModule()
    mod.name = "testhost"
    mod.host_suffixes = ("cdn.example.com",)
    url = "https://cdn.example.com/clip.mp4"
    assert mod.supports(url)

    with patch("providers.direct_media.head_content_type", return_value="video/mp4"):
        meta = mod.metadata(url)
    assert meta.platform == "testhost"
    assert meta.formats[0].id == "original"
    assert meta.formats[0].url == url

    dest = tmp_path / "out.mp4"
    with (
        patch("providers.direct_media.head_content_type", return_value="video/mp4"),
        patch("providers.direct_media.download_file", return_value=(12, "video/mp4")) as dl,
    ):
        result = mod.download(url, "original", dest)
    dl.assert_called_once()
    assert result.format_id == "original"
    assert result.filesize == 12


def test_platform_module_page_url_not_configured():
    mod = PlatformModule()
    mod.name = "youtube"
    mod.host_suffixes = ("youtube.com", "www.youtube.com")
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    assert mod.supports(url)
    with pytest.raises(ProviderNotConfiguredError):
        mod.metadata(url)
    with pytest.raises(ProviderNotConfiguredError):
        mod.download(url, "original", Path("/tmp/x.mp4"))


def test_registry_youtube_page_not_configured():
    reset_registry()
    from packages.registry.providers import get_registry

    registry = get_registry()
    provider = registry.resolve("https://www.youtube.com/watch?v=abc123")
    assert provider.name == "youtube"
    with pytest.raises(ProviderNotConfiguredError):
        provider.metadata("https://www.youtube.com/watch?v=abc123")


def test_build_platform_modules_alias():
    modules = build_platform_modules()
    assert any(m.name == "youtube" for m in modules)


@pytest.mark.parametrize(
    ("url", "platform"),
    [
        ("https://www.imdb.com/video/vi123.mp4", "imdb"),
        ("https://www.moviepilot.de/trailers/clip.mp4", "moviepilot"),
        ("https://www.rottentomatoes.com/media/trailer.mp4", "rottentomatoes"),
    ],
)
def test_movie_modules_resolve_and_download_direct_media(
    tmp_path: Path, url: str, platform: str
):
    """Download service uses PlatformModule for movie hosts (direct media)."""
    reset_registry()
    from packages.engine.engine import MediaCoreEngine
    from packages.registry.providers import get_registry

    registry = get_registry()
    provider = registry.resolve(url)
    assert provider.name == platform
    assert "download" in provider.capabilities.to_list()

    with patch("providers.direct_media.head_content_type", return_value="video/mp4"):
        meta = provider.metadata(url)
    assert meta.platform == platform

    dest = tmp_path / "movie.mp4"
    engine = MediaCoreEngine(registry=registry)
    with (
        patch("providers.direct_media.head_content_type", return_value="video/mp4"),
        patch("providers.direct_media.download_file", return_value=(8, "video/mp4")),
    ):
        result = engine.download(url, "original", dest)
    assert result.format_id == "original"
    assert result.filesize == 8


@pytest.mark.parametrize(
    "url",
    [
        "https://www.imdb.com/video/vi2524815897",
        "https://www.moviepilot.de/movies/interstellar-2/trailer",
        "https://www.rottentomatoes.com/m/interstellar",
    ],
)
def test_movie_modules_page_urls_not_configured(url: str):
    reset_registry()
    from packages.registry.providers import get_registry

    provider = get_registry().resolve(url)
    assert provider.name in {"imdb", "moviepilot", "rottentomatoes"}
    with pytest.raises(ProviderNotConfiguredError):
        provider.metadata(url)
