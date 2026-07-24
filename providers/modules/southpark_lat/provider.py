"""Auto-generated MediaCore platform module for `southpark.lat`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SouthparkLatProvider(PlatformModule):
    name = 'southpark.lat'
    status = 'not_configured'
    host_suffixes = ('southpark.lat',)
    ie_names = ('southpark.lat',)
    source = "catalog"
    description = 'Platform module for southpark.lat'
