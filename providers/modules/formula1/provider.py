"""Auto-generated MediaCore platform module for `formula1`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Formula1Provider(PlatformModule):
    name = 'formula1'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Formula1',)
    source = "catalog"
    description = 'Platform module for formula1'
