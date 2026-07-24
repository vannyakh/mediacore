"""Auto-generated MediaCore platform module for `ukcolumn`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class UkcolumnProvider(PlatformModule):
    name = 'ukcolumn'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('ukcolumn',)
    source = "catalog"
    description = 'Platform module for ukcolumn'
