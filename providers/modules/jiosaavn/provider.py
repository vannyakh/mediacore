"""Auto-generated MediaCore platform module for `jiosaavn`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class JiosaavnProvider(PlatformModule):
    name = 'jiosaavn'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('jiosaavn:album', 'jiosaavn:artist', 'jiosaavn:playlist', 'jiosaavn:show', 'jiosaavn:\u200bshow:playlist', 'jiosaavn:song')
    source = "catalog"
    description = 'Platform module for jiosaavn'
