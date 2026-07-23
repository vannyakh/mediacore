"""Auto-generated MediaCore catalog stub for `palcomp3`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Palcomp3Provider(StubProvider):
    name = 'palcomp3'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('PalcoMP3:artist', 'PalcoMP3:song', 'PalcoMP3:video')
    source = "catalog"
    description = 'Catalog stub for palcomp3'
