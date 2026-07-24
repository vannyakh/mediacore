"""Auto-generated MediaCore platform module for `digiview`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class DigiviewProvider(PlatformModule):
    name = 'digiview'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Digiview',)
    source = "catalog"
    description = 'Platform module for digiview'
