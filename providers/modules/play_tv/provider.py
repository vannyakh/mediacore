"""Auto-generated MediaCore platform module for `play.tv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class PlayTvProvider(PlatformModule):
    name = 'play.tv'
    status = 'not_configured'
    host_suffixes = ('play.tv',)
    ie_names = ('play.tv',)
    source = "catalog"
    description = 'PLAY (formerly goplay.be)'
