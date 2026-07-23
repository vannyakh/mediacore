"""Auto-generated MediaCore catalog stub for `bitchute`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BitchuteProvider(StubProvider):
    name = 'bitchute'
    status = 'not_configured'
    host_suffixes = ('bitchute.com', 'www.bitchute.com')
    ie_names = ('BitChute',)
    source = "catalog"
    description = 'Catalog stub for bitchute'
