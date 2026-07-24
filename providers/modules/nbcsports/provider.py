"""Auto-generated MediaCore platform module for `nbcsports`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NbcsportsProvider(PlatformModule):
    name = 'nbcsports'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('NBCSports',)
    source = "catalog"
    description = 'Platform module for nbcsports'
