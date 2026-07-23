"""Auto-generated MediaCore catalog stub for `24tv.ua`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P24tvUaProvider(StubProvider):
    name = '24tv.ua'
    status = 'not_configured'
    host_suffixes = ('24tv.ua',)
    ie_names = ('24tv.ua',)
    source = "catalog"
    description = 'Catalog stub for 24tv.ua'
