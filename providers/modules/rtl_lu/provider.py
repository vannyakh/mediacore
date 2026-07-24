"""Auto-generated MediaCore platform module for `rtl.lu`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RtlLuProvider(PlatformModule):
    name = 'rtl.lu'
    status = 'not_configured'
    host_suffixes = ('rtl.lu',)
    ie_names = ('rtl.lu:article', 'rtl.lu:tele-vod')
    source = "catalog"
    description = 'Platform module for rtl.lu'
