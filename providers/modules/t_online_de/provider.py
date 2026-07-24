"""Auto-generated MediaCore platform module for `t-online.de`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class TOnlineDeProvider(PlatformModule):
    name = 't-online.de'
    status = 'broken'
    host_suffixes = ('t-online.de',)
    ie_names = ('t-online.de',)
    source = "catalog"
    description = 'Platform module for t-online.de'
