"""Auto-generated MediaCore platform module for `tv8.it`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Tv8ItProvider(PlatformModule):
    name = 'tv8.it'
    status = 'not_configured'
    host_suffixes = ('tv8.it',)
    ie_names = ('tv8.it', 'tv8.it:live', 'tv8.it:playlist')
    source = "catalog"
    description = 'TV8 Live'
