"""Auto-generated MediaCore catalog stub for `metacritic`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MetacriticProvider(StubProvider):
    name = 'metacritic'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Metacritic',)
    source = "catalog"
    description = 'Catalog stub for metacritic'
