"""Auto-generated MediaCore platform module for `sky.it`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SkyItProvider(PlatformModule):
    name = 'sky.it'
    status = 'not_configured'
    host_suffixes = ('sky.it',)
    ie_names = ('sky.it',)
    source = "catalog"
    description = 'Platform module for sky.it'
