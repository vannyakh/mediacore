"""Auto-generated MediaCore platform module for `20min`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class P20minProvider(PlatformModule):
    name = '20min'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('20min',)
    source = "catalog"
    description = 'Platform module for 20min'
