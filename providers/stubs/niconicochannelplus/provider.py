"""Auto-generated MediaCore catalog stub for `niconicochannelplus`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NiconicochannelplusProvider(StubProvider):
    name = 'niconicochannelplus'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('NiconicoChannelPlus', 'NiconicoChannelPlus:\u200bchannel:lives', 'NiconicoChannelPlus:\u200bchannel:videos')
    source = "catalog"
    description = 'ニコニコチャンネルプラス'
