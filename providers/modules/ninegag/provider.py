"""Auto-generated MediaCore platform module for `ninegag`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NinegagProvider(PlatformModule):
    name = 'ninegag'
    status = 'not_configured'
    host_suffixes = ('9gag.com', 'www.9gag.com')
    ie_names = ('9gag',)
    source = "catalog"
    description = '9GAG'
