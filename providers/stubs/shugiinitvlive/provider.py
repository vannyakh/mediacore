"""Auto-generated MediaCore catalog stub for `shugiinitvlive`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ShugiinitvliveProvider(StubProvider):
    name = 'shugiinitvlive'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ShugiinItvLive',)
    source = "catalog"
    description = '衆議院インターネット審議中継'
