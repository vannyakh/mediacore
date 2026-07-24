"""Auto-generated MediaCore platform module for `tass`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class TassProvider(PlatformModule):
    name = 'tass'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Tass',)
    source = "catalog"
    description = 'Platform module for tass'
