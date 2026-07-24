"""Auto-generated MediaCore platform module for `voicy`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class VoicyProvider(PlatformModule):
    name = 'voicy'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('voicy', 'voicy:channel')
    source = "catalog"
    description = 'Platform module for voicy'
