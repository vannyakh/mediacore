"""Auto-generated MediaCore catalog stub for `cbslocal`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CbslocalProvider(StubProvider):
    name = 'cbslocal'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('CBSLocal',)
    source = "catalog"
    description = 'Catalog stub for cbslocal'
