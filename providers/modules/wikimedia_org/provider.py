"""Auto-generated MediaCore platform module for `wikimedia.org`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class WikimediaOrgProvider(PlatformModule):
    name = 'wikimedia.org'
    status = 'not_configured'
    host_suffixes = ('wikimedia.org',)
    ie_names = ('wikimedia.org',)
    source = "catalog"
    description = 'Platform module for wikimedia.org'
