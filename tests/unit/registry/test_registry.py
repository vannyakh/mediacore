import pytest

from packages.registry.providers import build_default_registry
from providers.generic.provider import GenericHTTPProvider
from providers.vimeo.provider import VimeoProvider

pytestmark = pytest.mark.unit


def test_registry_resolves_generic_media():
    registry = build_default_registry()
    provider = registry.resolve("https://cdn.example.com/clip.mp4")
    assert isinstance(provider, GenericHTTPProvider)


def test_registry_resolves_vimeo():
    registry = build_default_registry()
    provider = registry.resolve("https://vimeo.com/123456")
    assert isinstance(provider, VimeoProvider)


def test_platforms_include_builtins():
    names = {p["name"] for p in build_default_registry().platforms()}
    assert {"generic", "vimeo", "filesystem", "example"}.issubset(names)
