"""Auto-generated MediaCore catalog stub for `sport5`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Sport5Provider(StubProvider):
    name = 'sport5'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Sport5',)
    source = "catalog"
    description = 'Catalog stub for sport5'
