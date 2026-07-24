"""Auto-generated MediaCore platform module for `ndtv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NdtvProvider(PlatformModule):
    name = 'ndtv'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('NDTV',)
    source = "catalog"
    description = 'Platform module for ndtv'
