"""Auto-generated MediaCore platform module for `247sports`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class P247sportsProvider(PlatformModule):
    name = '247sports'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('247sports',)
    source = "catalog"
    description = 'Platform module for 247sports'
