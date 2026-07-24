"""Auto-generated MediaCore platform module for `nts.live`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NtsLiveProvider(PlatformModule):
    name = 'nts.live'
    status = 'not_configured'
    host_suffixes = ('nts.live',)
    ie_names = ('nts.live',)
    source = "catalog"
    description = 'Platform module for nts.live'
