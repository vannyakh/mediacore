"""Auto-generated MediaCore catalog stub for `n1info`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class N1infoProvider(StubProvider):
    name = 'n1info'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('N1Info:article',)
    source = "catalog"
    description = 'Catalog stub for n1info'
