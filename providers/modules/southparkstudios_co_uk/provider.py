"""Auto-generated MediaCore platform module for `southparkstudios.co.uk`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SouthparkstudiosCoUkProvider(PlatformModule):
    name = 'southparkstudios.co.uk'
    status = 'not_configured'
    host_suffixes = ('southparkstudios.co.uk',)
    ie_names = ('southparkstudios.co.uk',)
    source = "catalog"
    description = 'Platform module for southparkstudios.co.uk'
