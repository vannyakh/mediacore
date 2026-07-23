"""Auto-generated MediaCore catalog stub for `tv2article`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tv2articleProvider(StubProvider):
    name = 'tv2article'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('TV2Article',)
    source = "catalog"
    description = 'Catalog stub for tv2article'
