"""Auto-generated MediaCore catalog stub for `fox9news`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Fox9newsProvider(StubProvider):
    name = 'fox9news'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('FOX9News',)
    source = "catalog"
    description = 'Catalog stub for fox9news'
