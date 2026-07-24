"""Auto-generated MediaCore platform module for `youku`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class YoukuProvider(PlatformModule):
    name = 'youku'
    status = 'not_configured'
    host_suffixes = ('youku.com', 'v.youku.com', 'www.youku.com')
    ie_names = ('youku', 'youku:show')
    source = "catalog"
    description = '优酷'
