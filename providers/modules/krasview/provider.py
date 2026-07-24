"""Auto-generated MediaCore platform module for `krasview`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class KrasviewProvider(PlatformModule):
    name = 'krasview'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('KrasView',)
    source = "catalog"
    description = 'Красвью'
