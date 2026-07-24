"""Auto-generated MediaCore platform module for `ntv.ru`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NtvRuProvider(PlatformModule):
    name = 'ntv.ru'
    status = 'not_configured'
    host_suffixes = ('ntv.ru',)
    ie_names = ('ntv.ru',)
    source = "catalog"
    description = 'Platform module for ntv.ru'
