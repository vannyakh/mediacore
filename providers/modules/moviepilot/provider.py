"""Auto-generated MediaCore platform module for `moviepilot`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MoviepilotProvider(PlatformModule):
    name = 'moviepilot'
    status = 'not_configured'
    host_suffixes = ('moviepilot.de', 'www.moviepilot.de')
    ie_names = ('moviepilot',)
    source = "catalog"
    description = 'Moviepilot trailer'
