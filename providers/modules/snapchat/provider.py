"""Auto-generated MediaCore platform module for `snapchat`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SnapchatProvider(PlatformModule):
    name = 'snapchat'
    status = 'not_configured'
    host_suffixes = ('snapchat.com', 'www.snapchat.com', 'story.snapchat.com')
    ie_names = ('Snapchat',)
    source = "catalog"
    description = 'Platform module for snapchat'
