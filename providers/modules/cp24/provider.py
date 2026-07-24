"""Auto-generated MediaCore platform module for `cp24`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Cp24Provider(PlatformModule):
    name = 'cp24'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('cp24',)
    source = "catalog"
    description = 'Platform module for cp24'
