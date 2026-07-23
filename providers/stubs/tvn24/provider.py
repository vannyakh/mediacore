"""Auto-generated MediaCore catalog stub for `tvn24`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tvn24Provider(StubProvider):
    name = 'tvn24'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('TVN24',)
    source = "catalog"
    description = 'Catalog stub for tvn24'
