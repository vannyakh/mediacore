"""Auto-generated MediaCore platform module for `megaphone.fm`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MegaphoneFmProvider(PlatformModule):
    name = 'megaphone.fm'
    status = 'not_configured'
    host_suffixes = ('megaphone.fm',)
    ie_names = ('megaphone.fm',)
    source = "catalog"
    description = 'megaphone.fm embedded players'
