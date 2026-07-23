"""Auto-generated MediaCore catalog stub for `9news`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P9newsProvider(StubProvider):
    name = '9news'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('9News',)
    source = "catalog"
    description = 'Catalog stub for 9news'
