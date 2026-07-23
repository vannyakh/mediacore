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
        logger.debug("Registered provider: %s", provider.name)

    def clear(self) -> None:
        self._providers.clear()

    @property
    def providers(self) -> list[Provider]:
        return list(self._providers)

    def platforms(self) -> list[dict[str, str]]:
        return [{"name": p.name, "status": getattr(p, "status", "active")} for p in self._providers]

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


def build_default_registry() -> ProviderRegistry:
    registry = ProviderRegistry()
    # Built-in providers only — community providers should be separate packages.
    ordered_modules = [
        "providers.filesystem.provider",
        "providers.vimeo.provider",
        "providers.generic.provider",
        "providers.example.provider",
    ]
    for module_name in ordered_modules:
        try:
            module = importlib.import_module(module_name)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Failed to load provider module %s: %s", module_name, exc)
            continue
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
    return registry


_default_registry: ProviderRegistry | None = None


def get_registry() -> ProviderRegistry:
    global _default_registry
    if _default_registry is None:
        _default_registry = build_default_registry()
    return _default_registry
