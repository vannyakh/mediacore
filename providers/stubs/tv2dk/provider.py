"""Auto-generated MediaCore catalog stub for `tv2dk`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tv2dkProvider(StubProvider):
    name = 'tv2dk'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('TV2DK',)
    source = "catalog"
    description = 'Catalog stub for tv2dk'
