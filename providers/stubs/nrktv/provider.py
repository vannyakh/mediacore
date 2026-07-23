"""Auto-generated MediaCore catalog stub for `nrktv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NrktvProvider(StubProvider):
    name = 'nrktv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('NRKTV',)
    source = "catalog"
    description = 'NRK TV and NRK Radio'
