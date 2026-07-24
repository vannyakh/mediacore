"""Auto-generated MediaCore platform module for `rumble`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RumbleProvider(PlatformModule):
    name = 'rumble'
    status = 'not_configured'
    host_suffixes = ('rumble.com', 'www.rumble.com')
    ie_names = ('Rumble',)
    source = "catalog"
    description = 'Platform module for rumble'
