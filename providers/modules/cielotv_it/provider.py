"""Auto-generated MediaCore platform module for `cielotv.it`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class CielotvItProvider(PlatformModule):
    name = 'cielotv.it'
    status = 'not_configured'
    host_suffixes = ('cielotv.it', 'www.cielotv.it')
    ie_names = ('cielotv.it',)
    source = "catalog"
    description = 'Platform module for cielotv.it'
