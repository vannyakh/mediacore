"""Auto-generated MediaCore platform module for `weibo`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class WeiboProvider(PlatformModule):
    name = 'weibo'
    status = 'not_configured'
    host_suffixes = ('weibo.com', 'www.weibo.com', 'video.weibo.com')
    ie_names = ('Weibo',)
    source = "catalog"
    description = 'Platform module for weibo'
