"""Auto-generated MediaCore platform module for `nrltv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NrltvProvider(PlatformModule):
    name = 'nrltv'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('NRLTV',)
    source = "catalog"
    description = 'Platform module for nrltv'
