"""Auto-generated MediaCore platform module for `56.com`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class P56ComProvider(PlatformModule):
    name = '56.com'
    status = 'not_configured'
    host_suffixes = ('56.com', 'www.56.com', 'player.56.com')
    ie_names = ('56.com',)
    source = "catalog"
    description = 'Platform module for 56.com'
