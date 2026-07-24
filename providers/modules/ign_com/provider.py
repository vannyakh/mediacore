"""Auto-generated MediaCore platform module for `ign.com`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class IgnComProvider(PlatformModule):
    name = 'ign.com'
    status = 'not_configured'
    host_suffixes = ('ign.com',)
    ie_names = ('ign.com',)
    source = "catalog"
    description = 'Platform module for ign.com'
