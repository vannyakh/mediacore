"""Auto-generated MediaCore platform module for `frontendmasters`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class FrontendmastersProvider(PlatformModule):
    name = 'frontendmasters'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('FrontendMasters',)
    source = "catalog"
    description = 'Platform module for frontendmasters'
