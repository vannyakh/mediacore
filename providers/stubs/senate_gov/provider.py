"""Auto-generated MediaCore catalog stub for `senate.gov`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SenateGovProvider(StubProvider):
    name = 'senate.gov'
    status = 'not_configured'
    host_suffixes = ('senate.gov',)
    ie_names = ('senate.gov', 'senate.gov:isvp')
    source = "catalog"
    description = 'Catalog stub for senate.gov'
