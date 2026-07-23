"""Auto-generated MediaCore catalog stub for `cbs`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CbsProvider(StubProvider):
    name = 'cbs'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('CBS',)
    source = "catalog"
    description = 'Catalog stub for cbs'
