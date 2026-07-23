"""Auto-generated MediaCore catalog stub for `9now.com.au`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P9nowComAuProvider(StubProvider):
    name = '9now.com.au'
    status = 'not_configured'
    host_suffixes = ('9now.com.au',)
    ie_names = ('9now.com.au',)
    source = "catalog"
    description = 'Catalog stub for 9now.com.au'
