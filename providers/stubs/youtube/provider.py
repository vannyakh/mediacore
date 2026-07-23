"""Auto-generated MediaCore catalog stub for `youtube`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class YoutubeProvider(StubProvider):
    name = 'youtube'
    status = 'not_configured'
    host_suffixes = ('youtube.com', 'youtu.be', 'youtube-nocookie.com', 'm.youtube.com', 'music.youtube.com', 'www.youtube.com')
    ie_names = ('youtube', 'Youtube', 'YoutubeTab', 'YoutubeClip', 'youtube:clip', 'youtube:favorites', 'youtube:history', 'youtube:\u200bmusic:search_url', 'youtube:notif', 'youtube:playlist', 'youtube:recommended', 'youtube:search', 'youtube:search_url', 'youtube:\u200bshorts:pivot:audio', 'youtube:subscriptions', 'youtube:tab', 'youtube:user', 'youtube:watchlater')
    source = "catalog"
    description = 'YouTube'
