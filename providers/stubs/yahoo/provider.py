"""Auto-generated MediaCore catalog stub for `yahoo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class YahooProvider(StubProvider):
    name = 'yahoo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('yahoo', 'yahoo:japannews', 'yahoo:search')
    source = "catalog"
    description = 'Yahoo! Japan News'
