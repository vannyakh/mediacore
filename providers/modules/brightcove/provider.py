"""Auto-generated MediaCore platform module for `brightcove`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class BrightcoveProvider(PlatformModule):
    name = 'brightcove'
    status = 'not_configured'
    host_suffixes = ('brightcove.com', 'players.brightcove.net')
    ie_names = ('brightcove:legacy', 'Brightcove', 'brightcove:new')
    source = "catalog"
    description = 'Platform module for brightcove'
