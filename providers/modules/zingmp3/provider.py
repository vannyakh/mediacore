"""Auto-generated MediaCore platform module for `zingmp3`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Zingmp3Provider(PlatformModule):
    name = 'zingmp3'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('zingmp3', 'zingmp3:album', 'zingmp3:chart-home', 'zingmp3:chart-music-video', 'zingmp3:hub', 'zingmp3:liveradio', 'zingmp3:podcast', 'zingmp3:podcast-episode', 'zingmp3:user', 'zingmp3:week-chart')
    source = "catalog"
    description = 'zingmp3.vn'
