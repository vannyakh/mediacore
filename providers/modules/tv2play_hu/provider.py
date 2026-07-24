"""Auto-generated MediaCore platform module for `tv2play.hu`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Tv2playHuProvider(PlatformModule):
    name = 'tv2play.hu'
    status = 'not_configured'
    host_suffixes = ('tv2play.hu',)
    ie_names = ('tv2play.hu',)
    source = "catalog"
    description = 'Platform module for tv2play.hu'
