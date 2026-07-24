"""Optional bridge from the plugin layer to the provider registry."""

from __future__ import annotations

from typing import Any

from packages.core.provider import Provider
from packages.registry.providers import get_registry

PLUGIN = {
    "name": "mediacore-plugin-provider",
    "version": "0.1.0",
    "kind": "provider",
    "description": (
        "Provider-plugin bridge: resolve URLs via packages.registry. "
        "Platform extractors remain under providers/."
    ),
    "status": "available",
    "capabilities": ["resolve", "metadata", "download"],
}


class ProviderBridge:
    def resolve(self, url: str) -> Provider:
        return get_registry().resolve(url)

    def metadata(self, url: str) -> Any:
        return self.resolve(url).metadata(url)

    def platforms(self) -> list[dict]:
        return get_registry().platforms()


def create(settings: Any | None = None) -> ProviderBridge:
    del settings
    return ProviderBridge()
