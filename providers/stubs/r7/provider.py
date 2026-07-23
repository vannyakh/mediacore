"""Auto-generated MediaCore catalog stub for `r7`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class R7Provider(StubProvider):
    name = 'r7'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('R7',)
    source = "catalog"
    description = 'Catalog stub for r7'
