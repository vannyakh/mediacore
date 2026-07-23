"""Auto-generated MediaCore catalog stub for `nhl.com`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NhlComProvider(StubProvider):
    name = 'nhl.com'
    status = 'not_configured'
    host_suffixes = ('nhl.com',)
    ie_names = ('nhl.com',)
    source = "catalog"
    description = 'Catalog stub for nhl.com'
