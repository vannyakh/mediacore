"""Auto-generated MediaCore platform module for `jwplatform`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class JwplatformProvider(PlatformModule):
    name = 'jwplatform'
    status = 'not_configured'
    host_suffixes = ('jwplatform.com', 'cdn.jwplayer.com')
    ie_names = ('JWPlatform',)
    source = "catalog"
    description = 'Platform module for jwplatform'
