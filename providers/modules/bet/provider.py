"""Auto-generated MediaCore platform module for `bet`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class BetProvider(PlatformModule):
    name = 'bet'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Bet',)
    source = "catalog"
    description = 'Platform module for bet'
