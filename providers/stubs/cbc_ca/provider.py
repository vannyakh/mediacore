"""Auto-generated MediaCore catalog stub for `cbc.ca`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CbcCaProvider(StubProvider):
    name = 'cbc.ca'
    status = 'not_configured'
    host_suffixes = ('cbc.ca',)
    ie_names = ('cbc.ca', 'cbc.ca:listen', 'cbc.ca:player', 'cbc.ca:\u200bplayer:playlist')
    source = "catalog"
    description = 'Catalog stub for cbc.ca'
