"""Auto-generated MediaCore catalog stub for `tube8`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tube8Provider(StubProvider):
    name = 'tube8'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Tube8',)
    source = "catalog"
    description = 'Catalog stub for tube8'
