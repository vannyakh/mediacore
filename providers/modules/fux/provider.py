"""Auto-generated MediaCore platform module for `fux`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class FuxProvider(PlatformModule):
    name = 'fux'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Fux',)
    source = "catalog"
    description = 'Platform module for fux'
