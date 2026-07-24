"""Auto-generated MediaCore platform module for `tiktok`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class TiktokProvider(PlatformModule):
    name = 'tiktok'
    status = 'broken'
    host_suffixes = ('tiktok.com', 'www.tiktok.com', 'vm.tiktok.com', 'm.tiktok.com')
    ie_names = ('TikTok', 'tiktok', 'tiktok:collection', 'tiktok:effect', 'tiktok:live', 'tiktok:sound', 'tiktok:tag', 'tiktok:user')
    source = "catalog"
    description = 'Platform module for tiktok'
