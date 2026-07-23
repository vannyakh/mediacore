"""Auto-generated MediaCore catalog stub for `katsomo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class KatsomoProvider(StubProvider):
    name = 'katsomo'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Katsomo',)
    source = "catalog"
    description = 'Catalog stub for katsomo'
