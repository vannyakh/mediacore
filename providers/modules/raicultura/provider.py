"""Auto-generated MediaCore platform module for `raicultura`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RaiculturaProvider(PlatformModule):
    name = 'raicultura'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('RaiCultura',)
    source = "catalog"
    description = 'Platform module for raicultura'
