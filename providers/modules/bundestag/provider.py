"""Auto-generated MediaCore platform module for `bundestag`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class BundestagProvider(PlatformModule):
    name = 'bundestag'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Bundestag',)
    source = "catalog"
    description = 'Platform module for bundestag'
