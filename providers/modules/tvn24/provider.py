"""Auto-generated MediaCore platform module for `tvn24`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Tvn24Provider(PlatformModule):
    name = 'tvn24'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('TVN24',)
    source = "catalog"
    description = 'Platform module for tvn24'
