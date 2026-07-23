"""Auto-generated MediaCore catalog stub for `playtvak`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PlaytvakProvider(StubProvider):
    name = 'playtvak'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Playtvak',)
    source = "catalog"
    description = 'Playtvak.cz, iDNES.cz and Lidovky.cz'
