"""Auto-generated MediaCore catalog stub for `nfhsnetwork`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NfhsnetworkProvider(StubProvider):
    name = 'nfhsnetwork'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('NFHSNetwork',)
    source = "catalog"
    description = 'Catalog stub for nfhsnetwork'
