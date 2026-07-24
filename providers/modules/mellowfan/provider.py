"""Auto-generated MediaCore platform module for `mellowfan`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MellowfanProvider(PlatformModule):
    name = 'mellowfan'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('mellowfan', 'mellowfan:capture', 'mellowfan:channel', 'mellowfan:\u200bchannel:search', 'mellowfan:movie', 'mellowfan:playlist')
    source = "catalog"
    description = 'mellow-fan'
