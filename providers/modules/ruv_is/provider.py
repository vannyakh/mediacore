"""Auto-generated MediaCore platform module for `ruv.is`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RuvIsProvider(PlatformModule):
    name = 'ruv.is'
    status = 'not_configured'
    host_suffixes = ('ruv.is',)
    ie_names = ('ruv.is:spila',)
    source = "catalog"
    description = 'Platform module for ruv.is'
