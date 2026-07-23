import pytest

from packages.registry.providers import build_default_registry, reset_registry
from providers.catalog import catalog_summary, search_extractors
from providers.platforms.factory import build_all_providers, build_platform_stubs

pytestmark = pytest.mark.provider


def test_catalog_summary_counts():
    summary = catalog_summary()
    assert summary["extractors"] >= 1000
    assert summary["providers_indexed"] >= 1000
    assert summary["providers_with_hosts"] >= 50


def test_search_youtube():
    hits = search_extractors("youtube")
    assert any("youtube" in h["ie_name"].lower() for h in hits)


def test_all_providers_generated():
    all_providers = build_all_providers()
    assert len(all_providers) >= 1000
    names = {p.name for p in all_providers}
    assert "youtube" in names
    assert "tiktok" in names


def test_host_stubs_resolve():
    stubs = build_platform_stubs()
    assert any(s.name == "youtube" for s in stubs)


def test_registry_resolves_youtube_stub():
    reset_registry()
    registry = build_default_registry()
    provider = registry.resolve("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    assert provider.name == "youtube"
    assert provider.status == "not_configured"


def test_registry_includes_full_catalog():
    reset_registry()
    registry = build_default_registry()
    assert len(registry.providers) >= 1000
