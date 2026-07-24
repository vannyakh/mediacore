"""Auto-generated MediaCore platform module for `twitter`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class TwitterProvider(PlatformModule):
    name = 'twitter'
    status = 'not_configured'
    host_suffixes = ('twitter.com', 'www.twitter.com', 'x.com', 'www.x.com', 'mobile.twitter.com')
    ie_names = ('twitter', 'Twitter', 'twitter:amplify', 'twitter:broadcast', 'twitter:card', 'twitter:shortener', 'twitter:spaces')
    source = "catalog"
    description = 'Platform module for twitter'
