"""Auto-generated MediaCore catalog stub for `karaoketv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class KaraoketvProvider(StubProvider):
    name = 'karaoketv'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Karaoketv',)
    source = "catalog"
    description = 'Catalog stub for karaoketv'
