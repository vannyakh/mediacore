"""Auto-generated MediaCore catalog stub for `tvopengr`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TvopengrProvider(StubProvider):
    name = 'tvopengr'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('tvopengr:embed', 'tvopengr:watch')
    source = "catalog"
    description = 'tvopen.gr embedded videos'
