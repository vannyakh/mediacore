"""Auto-generated MediaCore platform module for `palcomp3`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Palcomp3Provider(PlatformModule):
    name = 'palcomp3'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('PalcoMP3:artist', 'PalcoMP3:song', 'PalcoMP3:video')
    source = "catalog"
    description = 'Platform module for palcomp3'
