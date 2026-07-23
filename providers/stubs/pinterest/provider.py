"""Auto-generated MediaCore catalog stub for `pinterest`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PinterestProvider(StubProvider):
    name = 'pinterest'
    status = 'not_configured'
    host_suffixes = ('pinterest.com', 'www.pinterest.com', 'pin.it')
    ie_names = ('Pinterest',)
    source = "catalog"
    description = 'Catalog stub for pinterest'
