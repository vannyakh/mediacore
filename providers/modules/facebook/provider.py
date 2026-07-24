"""Auto-generated MediaCore platform module for `facebook`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class FacebookProvider(PlatformModule):
    name = 'facebook'
    status = 'not_configured'
    host_suffixes = ('facebook.com', 'www.facebook.com', 'fb.watch', 'm.facebook.com', 'fb.com', 'web.facebook.com')
    ie_names = ('facebook', 'Facebook', 'facebook:ads', 'facebook:reel')
    source = "catalog"
    description = 'Platform module for facebook'
