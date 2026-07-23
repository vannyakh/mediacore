"""Auto-generated MediaCore catalog stub for `salttvlive`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SalttvliveProvider(StubProvider):
    name = 'salttvlive'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('SaltTVLive',)
    source = "catalog"
    description = 'Catalog stub for salttvlive'
