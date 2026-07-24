"""Auto-generated MediaCore platform module for `rottentomatoes`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RottentomatoesProvider(PlatformModule):
    name = 'rottentomatoes'
    status = 'not_configured'
    host_suffixes = ('rottentomatoes.com', 'www.rottentomatoes.com')
    ie_names = ('RottenTomatoes',)
    source = "catalog"
    description = 'Platform module for rottentomatoes'
