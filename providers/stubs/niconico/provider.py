"""Auto-generated MediaCore catalog stub for `niconico`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NiconicoProvider(StubProvider):
    name = 'niconico'
    status = 'not_configured'
    host_suffixes = ('nicovideo.jp', 'www.nicovideo.jp', 'nico.ms')
    ie_names = ('niconico', 'Niconico', 'niconico:history', 'niconico:live', 'niconico:playlist', 'niconico:series', 'niconico:tag')
    source = "catalog"
    description = 'ニコニコ動画'
