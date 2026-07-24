"""Auto-generated MediaCore platform module for `twitch`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class TwitchProvider(PlatformModule):
    name = 'twitch'
    status = 'not_configured'
    host_suffixes = ('twitch.tv', 'www.twitch.tv', 'm.twitch.tv', 'clips.twitch.tv')
    ie_names = ('twitch:clips', 'Twitch', 'TwitchVod', 'TwitchClips', 'twitch:collection', 'twitch:stream', 'twitch:videos', 'twitch:\u200bvideos:clips', 'twitch:\u200bvideos:collections', 'twitch:vod')
    source = "catalog"
    description = 'Platform module for twitch'
