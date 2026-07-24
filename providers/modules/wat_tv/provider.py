"""Auto-generated MediaCore platform module for `wat.tv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class WatTvProvider(PlatformModule):
    name = 'wat.tv'
    status = 'not_configured'
    host_suffixes = ('wat.tv',)
    ie_names = ('wat.tv',)
    source = "catalog"
    description = 'Platform module for wat.tv'
