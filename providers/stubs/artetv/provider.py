"""Auto-generated MediaCore catalog stub for `artetv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ArtetvProvider(StubProvider):
    name = 'artetv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ArteTV',)
    source = "catalog"
    description = 'Catalog stub for artetv'
