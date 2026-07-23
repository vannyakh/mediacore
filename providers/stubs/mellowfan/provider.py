"""Auto-generated MediaCore catalog stub for `mellowfan`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MellowfanProvider(StubProvider):
    name = 'mellowfan'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('mellowfan', 'mellowfan:capture', 'mellowfan:channel', 'mellowfan:\u200bchannel:search', 'mellowfan:movie', 'mellowfan:playlist')
    source = "catalog"
    description = 'mellow-fan'
