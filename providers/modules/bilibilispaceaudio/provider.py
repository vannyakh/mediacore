"""Auto-generated MediaCore platform module for `bilibilispaceaudio`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class BilibilispaceaudioProvider(PlatformModule):
    name = 'bilibilispaceaudio'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('BilibiliSpaceAudio',)
    source = "catalog"
    description = 'Platform module for bilibilispaceaudio'
