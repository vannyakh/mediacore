"""Auto-generated MediaCore catalog stub for `n1infoasset`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class N1infoassetProvider(StubProvider):
    name = 'n1infoasset'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('N1InfoAsset',)
    source = "catalog"
    description = 'Catalog stub for n1infoasset'
