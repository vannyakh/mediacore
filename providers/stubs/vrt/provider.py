"""Auto-generated MediaCore catalog stub for `vrt`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class VrtProvider(StubProvider):
    name = 'vrt'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('VRT',)
    source = "catalog"
    description = 'VRT NWS, Flanders News, Flandern Info and Sporza'
