"""Auto-generated MediaCore catalog stub for `vk`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class VkProvider(StubProvider):
    name = 'vk'
    status = 'not_configured'
    host_suffixes = ('vk.com', 'vk.ru', 'vkvideo.ru')
    ie_names = ('vk', 'VK', 'vk:uservideos', 'vk:wallpost')
    source = "catalog"
    description = 'VK'
