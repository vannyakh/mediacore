"""Auto-generated MediaCore catalog stub for `nba`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NbaProvider(StubProvider):
    name = 'nba'
    status = 'broken'
    host_suffixes = ('nba.com', 'www.nba.com')
    ie_names = ('nba', 'NBA', 'nba:channel', 'nba:embed', 'nba:watch', 'nba:\u200bwatch:collection', 'nba:\u200bwatch:embed')
    source = "catalog"
    description = 'Catalog stub for nba'
