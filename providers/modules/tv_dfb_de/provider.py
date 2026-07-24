"""Auto-generated MediaCore platform module for `tv.dfb.de`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class TvDfbDeProvider(PlatformModule):
    name = 'tv.dfb.de'
    status = 'not_configured'
    host_suffixes = ('tv.dfb.de',)
    ie_names = ('tv.dfb.de',)
    source = "catalog"
    description = 'Platform module for tv.dfb.de'
