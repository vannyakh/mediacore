"""Auto-generated MediaCore platform module for `vk`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class VkProvider(PlatformModule):
    name = 'vk'
    status = 'not_configured'
    host_suffixes = ('vk.com', 'vk.ru', 'vkvideo.ru')
    ie_names = ('vk', 'VK', 'vk:uservideos', 'vk:wallpost')
    source = "catalog"
    description = 'VK'
