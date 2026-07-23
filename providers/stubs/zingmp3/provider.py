"""Auto-generated MediaCore catalog stub for `zingmp3`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Zingmp3Provider(StubProvider):
    name = 'zingmp3'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('zingmp3', 'zingmp3:album', 'zingmp3:chart-home', 'zingmp3:chart-music-video', 'zingmp3:hub', 'zingmp3:liveradio', 'zingmp3:podcast', 'zingmp3:podcast-episode', 'zingmp3:user', 'zingmp3:week-chart')
    source = "catalog"
    description = 'zingmp3.vn'
