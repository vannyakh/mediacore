"""Auto-generated MediaCore catalog stub for `ku6`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Ku6Provider(StubProvider):
    name = 'ku6'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Ku6',)
    source = "catalog"
    description = 'Catalog stub for ku6'
