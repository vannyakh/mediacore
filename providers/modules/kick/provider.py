"""Auto-generated MediaCore platform module for `kick`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class KickProvider(PlatformModule):
    name = 'kick'
    status = 'not_configured'
    host_suffixes = ('kick.com', 'www.kick.com')
    ie_names = ('kick:clips', 'Kick', 'kick:live', 'kick:vod')
    source = "catalog"
    description = 'Platform module for kick'
