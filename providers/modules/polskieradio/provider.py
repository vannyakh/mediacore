"""Auto-generated MediaCore platform module for `polskieradio`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class PolskieradioProvider(PlatformModule):
    name = 'polskieradio'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('PolskieRadio', 'polskieradio:audition', 'polskieradio:category', 'polskieradio:legacy', 'polskieradio:player', 'polskieradio:podcast', 'polskieradio:\u200bpodcast:list')
    source = "catalog"
    description = 'Platform module for polskieradio'
