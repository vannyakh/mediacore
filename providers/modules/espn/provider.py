"""Auto-generated MediaCore platform module for `espn`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class EspnProvider(PlatformModule):
    name = 'espn'
    status = 'not_configured'
    host_suffixes = ('espn.com', 'www.espn.com')
    ie_names = ('ESPN',)
    source = "catalog"
    description = 'Platform module for espn'
