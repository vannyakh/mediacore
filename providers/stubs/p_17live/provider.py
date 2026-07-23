"""Auto-generated MediaCore catalog stub for `17live`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P17liveProvider(StubProvider):
    name = '17live'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('17live', '17live:clip', '17live:vod')
    source = "catalog"
    description = 'Catalog stub for 17live'
