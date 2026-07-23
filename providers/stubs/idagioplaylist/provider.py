"""Auto-generated MediaCore catalog stub for `idagioplaylist`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class IdagioplaylistProvider(StubProvider):
    name = 'idagioplaylist'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('IdagioPlaylist',)
    source = "catalog"
    description = 'Catalog stub for idagioplaylist'
