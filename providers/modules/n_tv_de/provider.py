"""Auto-generated MediaCore platform module for `n-tv.de`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NTvDeProvider(PlatformModule):
    name = 'n-tv.de'
    status = 'not_configured'
    host_suffixes = ('n-tv.de',)
    ie_names = ('n-tv.de',)
    source = "catalog"
    description = 'Platform module for n-tv.de'
