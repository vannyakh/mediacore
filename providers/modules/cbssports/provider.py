"""Auto-generated MediaCore platform module for `cbssports`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class CbssportsProvider(PlatformModule):
    name = 'cbssports'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('cbssports', 'cbssports:embed')
    source = "catalog"
    description = 'Platform module for cbssports'
