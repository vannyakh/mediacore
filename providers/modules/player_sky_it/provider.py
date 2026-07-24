"""Auto-generated MediaCore platform module for `player.sky.it`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class PlayerSkyItProvider(PlatformModule):
    name = 'player.sky.it'
    status = 'not_configured'
    host_suffixes = ('player.sky.it',)
    ie_names = ('player.sky.it',)
    source = "catalog"
    description = 'Platform module for player.sky.it'
