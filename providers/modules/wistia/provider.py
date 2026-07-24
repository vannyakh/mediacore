"""Auto-generated MediaCore platform module for `wistia`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class WistiaProvider(PlatformModule):
    name = 'wistia'
    status = 'not_configured'
    host_suffixes = ('wistia.com', 'www.wistia.com', 'fast.wistia.net')
    ie_names = ('Wistia',)
    source = "catalog"
    description = 'Platform module for wistia'
