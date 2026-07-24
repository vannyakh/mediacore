"""Auto-generated MediaCore platform module for `nfl.com`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NflComProvider(PlatformModule):
    name = 'nfl.com'
    status = 'not_configured'
    host_suffixes = ('nfl.com',)
    ie_names = ('nfl.com', 'nfl.com:article', 'nfl.com:\u200bplus:episode', 'nfl.com:\u200bplus:replay')
    source = "catalog"
    description = 'Platform module for nfl.com'
