"""Auto-generated MediaCore platform module for `yahoo`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class YahooProvider(PlatformModule):
    name = 'yahoo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('yahoo', 'yahoo:japannews', 'yahoo:search')
    source = "catalog"
    description = 'Yahoo! Japan News'
