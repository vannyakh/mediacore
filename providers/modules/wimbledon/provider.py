"""Auto-generated MediaCore platform module for `wimbledon`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class WimbledonProvider(PlatformModule):
    name = 'wimbledon'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Wimbledon',)
    source = "catalog"
    description = 'Platform module for wimbledon'
