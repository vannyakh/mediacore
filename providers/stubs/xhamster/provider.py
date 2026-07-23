"""Auto-generated MediaCore catalog stub for `xhamster`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class XhamsterProvider(StubProvider):
    name = 'xhamster'
    status = 'not_configured'
    host_suffixes = ('xhamster.com', 'www.xhamster.com')
    ie_names = ('XHamster',)
    source = "catalog"
    description = 'Catalog stub for xhamster'
