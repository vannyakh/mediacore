"""Auto-generated MediaCore platform module for `parliamentlive.tv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class ParliamentliveTvProvider(PlatformModule):
    name = 'parliamentlive.tv'
    status = 'not_configured'
    host_suffixes = ('parliamentlive.tv',)
    ie_names = ('parliamentlive.tv',)
    source = "catalog"
    description = 'UK parliament videos'
