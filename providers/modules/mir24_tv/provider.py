"""Auto-generated MediaCore platform module for `mir24.tv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Mir24TvProvider(PlatformModule):
    name = 'mir24.tv'
    status = 'not_configured'
    host_suffixes = ('mir24.tv',)
    ie_names = ('mir24.tv',)
    source = "catalog"
    description = 'Platform module for mir24.tv'
