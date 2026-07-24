"""Auto-generated MediaCore platform module for `dw`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class DwProvider(PlatformModule):
    name = 'dw'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('dw', 'dw:article')
    source = "catalog"
    description = 'Platform module for dw'
