"""Auto-generated MediaCore platform module for `youtube`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class YoutubeProvider(PlatformModule):
    name = 'youtube'
    status = 'not_configured'
    host_suffixes = ('youtube.com', 'youtu.be', 'youtube-nocookie.com', 'm.youtube.com', 'music.youtube.com', 'www.youtube.com')
    ie_names = ('youtube', 'Youtube', 'YoutubeTab', 'YoutubeClip', 'youtube:clip', 'youtube:favorites', 'youtube:history', 'youtube:\u200bmusic:search_url', 'youtube:notif', 'youtube:playlist', 'youtube:recommended', 'youtube:search', 'youtube:search_url', 'youtube:\u200bshorts:pivot:audio', 'youtube:subscriptions', 'youtube:tab', 'youtube:user', 'youtube:watchlater')
    source = "catalog"
    description = 'YouTube'
