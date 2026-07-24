"""Auto-generated MediaCore platform module for `niconico`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NiconicoProvider(PlatformModule):
    name = 'niconico'
    status = 'not_configured'
    host_suffixes = ('nicovideo.jp', 'www.nicovideo.jp', 'nico.ms')
    ie_names = ('niconico', 'Niconico', 'niconico:history', 'niconico:live', 'niconico:playlist', 'niconico:series', 'niconico:tag')
    source = "catalog"
    description = 'ニコニコ動画'
