"""Auto-generated MediaCore platform module for `senate.gov`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SenateGovProvider(PlatformModule):
    name = 'senate.gov'
    status = 'not_configured'
    host_suffixes = ('senate.gov',)
    ie_names = ('senate.gov', 'senate.gov:isvp')
    source = "catalog"
    description = 'Platform module for senate.gov'
