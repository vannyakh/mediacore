"""Auto-generated MediaCore catalog stub for `shugiinitvliveroom`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ShugiinitvliveroomProvider(StubProvider):
    name = 'shugiinitvliveroom'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ShugiinItvLiveRoom',)
    source = "catalog"
    description = '衆議院インターネット審議中継 (中継)'
