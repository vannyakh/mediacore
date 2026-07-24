"""Auto-generated MediaCore platform module for `youtubeytbe`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class YoutubeytbeProvider(PlatformModule):
    name = 'youtubeytbe'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('YoutubeYtBe',)
    source = "catalog"
    description = 'youtu.be'
