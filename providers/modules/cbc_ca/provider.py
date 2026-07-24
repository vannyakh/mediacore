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
    host_suffixes = ('cbc.ca', 'www.cbc.ca', 'gem.cbc.ca')
    ie_names = ('cbc.ca', 'cbc.ca:player', 'cbc.ca:player:playlist', 'cbc.ca:listen', 'gem.cbc.ca', 'gem.cbc.ca:playlist', 'gem.cbc.ca:live', 'cbc.ca:\u200bplayer:playlist', 'gem.cbc.ca:olympics')
    source = "catalog"
    description = 'Platform module for cbc.ca'
