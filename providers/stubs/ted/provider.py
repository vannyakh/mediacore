"""Auto-generated MediaCore catalog stub for `ted`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TedProvider(StubProvider):
    name = 'ted'
    status = 'not_configured'
    host_suffixes = ('ted.com', 'www.ted.com')
    ie_names = ('TED',)
    source = "catalog"
    description = 'Catalog stub for ted'
