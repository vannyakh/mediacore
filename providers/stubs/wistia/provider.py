"""Auto-generated MediaCore catalog stub for `wistia`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class WistiaProvider(StubProvider):
    name = 'wistia'
    status = 'not_configured'
    host_suffixes = ('wistia.com', 'www.wistia.com', 'fast.wistia.net')
    ie_names = ('Wistia',)
    source = "catalog"
    description = 'Catalog stub for wistia'
