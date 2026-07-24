"""Auto-generated MediaCore platform module for `media.ccc.de`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MediaCccDeProvider(PlatformModule):
    name = 'media.ccc.de'
    status = 'not_configured'
    host_suffixes = ('media.ccc.de',)
    ie_names = ('media.ccc.de', 'media.ccc.de:lists')
    source = "catalog"
    description = 'Platform module for media.ccc.de'
