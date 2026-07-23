"""Auto-generated MediaCore catalog stub for `23video`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P23videoProvider(StubProvider):
    name = '23video'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('23video',)
    source = "catalog"
    description = 'Catalog stub for 23video'
