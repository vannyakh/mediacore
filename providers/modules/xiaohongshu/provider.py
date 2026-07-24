"""Auto-generated MediaCore platform module for `xiaohongshu`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class XiaohongshuProvider(PlatformModule):
    name = 'xiaohongshu'
    status = 'not_configured'
    host_suffixes = ('xiaohongshu.com', 'www.xiaohongshu.com', 'xhslink.com')
    ie_names = ('XiaoHongShu',)
    source = "catalog"
    description = '小红书'
