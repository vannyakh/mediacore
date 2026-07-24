"""Auto-generated MediaCore platform module for `nick.com`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NickComProvider(PlatformModule):
    name = 'nick.com'
    status = 'not_configured'
    host_suffixes = ('nick.com',)
    ie_names = ('nick.com',)
    source = "catalog"
    description = 'Platform module for nick.com'
