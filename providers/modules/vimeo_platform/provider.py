"""Auto-generated MediaCore platform module for `vimeo_platform`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class VimeoPlatformProvider(PlatformModule):
    name = 'vimeo_platform'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('vimeo', 'Vimeo', 'vimeo:album', 'vimeo:channel', 'vimeo:event', 'vimeo:group', 'vimeo:likes', 'vimeo:ondemand', 'vimeo:pro', 'vimeo:review', 'vimeo:user', 'vimeo:watchlater')
    source = "catalog"
    description = 'Vimeo user likes'
