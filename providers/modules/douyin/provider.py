"""Auto-generated MediaCore platform module for `douyin`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class DouyinProvider(PlatformModule):
    name = 'douyin'
    status = 'not_configured'
    host_suffixes = ('douyin.com', 'www.douyin.com', 'v.douyin.com')
    ie_names = ('Douyin',)
    source = "catalog"
    description = 'Platform module for douyin'
