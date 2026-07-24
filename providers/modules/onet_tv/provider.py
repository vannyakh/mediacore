"""Auto-generated MediaCore platform module for `onet.tv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class OnetTvProvider(PlatformModule):
    name = 'onet.tv'
    status = 'not_configured'
    host_suffixes = ('onet.tv',)
    ie_names = ('onet.tv', 'onet.tv:channel')
    source = "catalog"
    description = 'Platform module for onet.tv'
