"""Auto-generated MediaCore platform module for `10play`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class P10playProvider(PlatformModule):
    name = '10play'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('10play', '10play:season')
    source = "catalog"
    description = 'Platform module for 10play'
