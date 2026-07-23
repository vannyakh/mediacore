"""Auto-generated MediaCore catalog stub for `zaikoeticket`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ZaikoeticketProvider(StubProvider):
    name = 'zaikoeticket'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ZaikoETicket',)
    source = "catalog"
    description = 'Catalog stub for zaikoeticket'
