"""Auto-generated MediaCore catalog stub for `10play`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P10playProvider(StubProvider):
    name = '10play'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('10play', '10play:season')
    source = "catalog"
    description = 'Catalog stub for 10play'
