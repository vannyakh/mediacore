"""Auto-generated MediaCore catalog stub for `vimeo_platform`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class VimeoPlatformProvider(StubProvider):
    name = 'vimeo_platform'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('vimeo', 'Vimeo', 'vimeo:album', 'vimeo:channel', 'vimeo:event', 'vimeo:group', 'vimeo:likes', 'vimeo:ondemand', 'vimeo:pro', 'vimeo:review', 'vimeo:user', 'vimeo:watchlater')
    source = "catalog"
    description = 'Vimeo user likes'
