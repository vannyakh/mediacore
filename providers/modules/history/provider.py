"""Auto-generated MediaCore platform module for `history`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class HistoryProvider(PlatformModule):
    name = 'history'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('history:player', 'history:topic')
    source = "catalog"
    description = 'History.com Topic'
