"""Auto-generated MediaCore platform module for `vice`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class ViceProvider(PlatformModule):
    name = 'vice'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('vice', 'vice:article', 'vice:show')
    source = "catalog"
    description = 'Platform module for vice'
