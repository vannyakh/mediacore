"""Auto-generated MediaCore platform module for `onet.pl`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class OnetPlProvider(PlatformModule):
    name = 'onet.pl'
    status = 'not_configured'
    host_suffixes = ('onet.pl',)
    ie_names = ('onet.pl',)
    source = "catalog"
    description = 'Platform module for onet.pl'
