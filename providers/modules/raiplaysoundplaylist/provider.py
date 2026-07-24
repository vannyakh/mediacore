"""Auto-generated MediaCore platform module for `raiplaysoundplaylist`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RaiplaysoundplaylistProvider(PlatformModule):
    name = 'raiplaysoundplaylist'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('RaiPlaySoundPlaylist',)
    source = "catalog"
    description = 'Platform module for raiplaysoundplaylist'
