"""Auto-generated MediaCore catalog stub for `twitch`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TwitchProvider(StubProvider):
    name = 'twitch'
    status = 'not_configured'
    host_suffixes = ('twitch.tv', 'www.twitch.tv', 'm.twitch.tv', 'clips.twitch.tv')
    ie_names = ('twitch:clips', 'Twitch', 'TwitchVod', 'TwitchClips', 'twitch:collection', 'twitch:stream', 'twitch:videos', 'twitch:\u200bvideos:clips', 'twitch:\u200bvideos:collections', 'twitch:vod')
    source = "catalog"
    description = 'Catalog stub for twitch'
