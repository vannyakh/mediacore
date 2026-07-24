"""Provider registry — core does not hardcode platform logic."""

from __future__ import annotations

import importlib
import logging

from packages.core.exceptions import UnsupportedURLError
from packages.core.provider import Provider

logger = logging.getLogger("mediacore.registry")


class ProviderRegistry:
    def __init__(self) -> None:
        self._providers: list[Provider] = []

    def register(self, provider: Provider) -> None:
        self._providers.append(provider)
        logger.debug("Registered provider: %s", getattr(provider, "name", provider))

    def clear(self) -> None:
        self._providers.clear()

    @property
    def providers(self) -> list[Provider]:
        return list(self._providers)

    def platforms(self) -> list[dict]:
        out = []
        for p in self._providers:
            caps = getattr(p, "capabilities", None)
            item = {
                "name": p.name,
                "status": getattr(p, "status", "active"),
                "capabilities": caps.to_list() if caps is not None else [],
            }
            source = getattr(p, "source", None)
            if source:
                item["source"] = source
            out.append(item)
        return out

    def resolve(self, url: str) -> Provider:
        for provider in self._providers:
            if provider.supports(url):
                return provider
        raise UnsupportedURLError(url)

    def get(self, name: str) -> Provider | None:
        for provider in self._providers:
            if provider.name == name:
                return provider
        return None


def _register_module(registry: ProviderRegistry, module_name: str) -> None:
    try:
        module = importlib.import_module(module_name)
    except Exception as exc:  # noqa: BLE001
        logger.warning("Failed to load provider module %s: %s", module_name, exc)
        return
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if (
            isinstance(attr, type)
            and issubclass(attr, Provider)
            and attr is not Provider
            and attr_name.endswith("Provider")
            and attr.__module__ == module.__name__
        ):
            registry.register(attr())
            break


def build_default_registry() -> ProviderRegistry:
    registry = ProviderRegistry()

    # Working providers first (same name as a catalog stub → stub is skipped)
    for module_name in (
        "providers.filesystem.provider",
        # Priority platforms (public oEmbed)
        "providers.youtube.provider",
        "providers.tiktok.provider",
        "providers.vimeo.provider",
        "providers.dailymotion.provider",
        "providers.soundcloud.provider",
        "providers.reddit.provider",
        "providers.ted.provider",
        "providers.wikimedia.provider",
        "providers.bandcamp.provider",
        "providers.mixcloud.provider",
        "providers.streamable.provider",
        "providers.imgur.provider",
        "providers.archiveorg.provider",
        "providers.flickr.provider",
        "providers.applepodcasts.provider",
        "providers.abc_net_au.provider",
        "providers.bbc.provider",
        "providers.bilibili.provider",
        "providers.bitchute.provider",
    ):
        _register_module(registry, module_name)

    # Catalog platform modules (folders under providers/modules/)
    try:
        from providers.platforms.factory import build_all_providers, catalog_package_count

        modules = build_all_providers()
        for module in modules:
            # Skip names already registered as working providers
            if registry.get(module.name):
                continue
            registry.register(module)
        logger.info(
            "Registered %s platform modules (%s on-disk packages)",
            len(modules),
            catalog_package_count(),
        )
    except Exception as exc:  # noqa: BLE001
        logger.warning("Failed to load catalog platform modules: %s", exc)

    # Generic direct media + example last
    for module_name in (
        "providers.generic.provider",
        "providers.example.provider",
    ):
        _register_module(registry, module_name)

    return registry


_default_registry: ProviderRegistry | None = None


def get_registry() -> ProviderRegistry:
    global _default_registry
    if _default_registry is None:
        _default_registry = build_default_registry()
    return _default_registry


def reset_registry() -> ProviderRegistry:
    global _default_registry
    _default_registry = build_default_registry()
    return _default_registry
