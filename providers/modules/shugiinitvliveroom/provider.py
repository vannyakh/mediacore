"""Auto-generated MediaCore platform module for `shugiinitvliveroom`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class ShugiinitvliveroomProvider(PlatformModule):
    name = 'shugiinitvliveroom'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ShugiinItvLiveRoom',)
    source = "catalog"
    description = '衆議院インターネット審議中継 (中継)'
