"""Auto-generated MediaCore catalog stub for `n-tv.de`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NTvDeProvider(StubProvider):
    name = 'n-tv.de'
    status = 'not_configured'
    host_suffixes = ('n-tv.de',)
    ie_names = ('n-tv.de',)
    source = "catalog"
    description = 'Catalog stub for n-tv.de'
