"""Auto-generated MediaCore platform module for `17live`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class P17liveProvider(PlatformModule):
    name = '17live'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('17live', '17live:clip', '17live:vod')
    source = "catalog"
    description = 'Platform module for 17live'
