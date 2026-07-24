"""Auto-generated MediaCore platform module for `noz`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NozProvider(PlatformModule):
    name = 'noz'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Noz',)
    source = "catalog"
    description = 'Platform module for noz'
