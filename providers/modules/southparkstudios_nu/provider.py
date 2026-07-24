"""Auto-generated MediaCore platform module for `southparkstudios.nu`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SouthparkstudiosNuProvider(PlatformModule):
    name = 'southparkstudios.nu'
    status = 'not_configured'
    host_suffixes = ('southparkstudios.nu',)
    ie_names = ('southparkstudios.nu',)
    source = "catalog"
    description = 'Platform module for southparkstudios.nu'
