"""Auto-generated MediaCore platform module for `nba`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NbaProvider(PlatformModule):
    name = 'nba'
    status = 'broken'
    host_suffixes = ('nba.com', 'www.nba.com')
    ie_names = ('nba', 'NBA', 'nba:channel', 'nba:embed', 'nba:watch', 'nba:\u200bwatch:collection', 'nba:\u200bwatch:embed')
    source = "catalog"
    description = 'Platform module for nba'
