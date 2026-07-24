"""Auto-generated MediaCore platform module for `southparkstudios.com.br`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SouthparkstudiosComBrProvider(PlatformModule):
    name = 'southparkstudios.com.br'
    status = 'not_configured'
    host_suffixes = ('southparkstudios.com.br',)
    ie_names = ('southparkstudios.com.br',)
    source = "catalog"
    description = 'Platform module for southparkstudios.com.br'
