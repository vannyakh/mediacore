"""Auto-generated MediaCore platform module for `cbc.ca`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class CbcCaProvider(PlatformModule):
    name = 'cbc.ca'
    status = 'not_configured'
    host_suffixes = ('cbc.ca',)
    ie_names = ('cbc.ca', 'cbc.ca:listen', 'cbc.ca:player', 'cbc.ca:\u200bplayer:playlist')
    source = "catalog"
    description = 'Platform module for cbc.ca'
