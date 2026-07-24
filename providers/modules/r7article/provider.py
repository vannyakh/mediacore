"""Auto-generated MediaCore platform module for `r7article`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class R7articleProvider(PlatformModule):
    name = 'r7article'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('R7Article',)
    source = "catalog"
    description = 'Platform module for r7article'
