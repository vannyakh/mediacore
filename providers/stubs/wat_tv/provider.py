"""Auto-generated MediaCore catalog stub for `wat.tv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class WatTvProvider(StubProvider):
    name = 'wat.tv'
    status = 'not_configured'
    host_suffixes = ('wat.tv',)
    ie_names = ('wat.tv',)
    source = "catalog"
    description = 'Catalog stub for wat.tv'
