"""Auto-generated MediaCore platform module for `tou.tv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class TouTvProvider(PlatformModule):
    name = 'tou.tv'
    status = 'not_configured'
    host_suffixes = ('tou.tv',)
    ie_names = ('tou.tv',)
    source = "catalog"
    description = 'Platform module for tou.tv'
