"""Auto-generated MediaCore platform module for `bilibili`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class BilibiliProvider(PlatformModule):
    name = 'bilibili'
    status = 'not_configured'
    host_suffixes = ('bilibili.com', 'www.bilibili.com', 'b23.tv', 'space.bilibili.com')
    ie_names = ('BiliBili', 'Bilibili')
    source = "catalog"
    description = 'Platform module for bilibili'
