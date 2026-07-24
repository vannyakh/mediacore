"""Auto-generated MediaCore platform module for `cu.ntv.co.jp`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class CuNtvCoJpProvider(PlatformModule):
    name = 'cu.ntv.co.jp'
    status = 'not_configured'
    host_suffixes = ('cu.ntv.co.jp',)
    ie_names = ('cu.ntv.co.jp',)
    source = "catalog"
    description = '日テレ無料TADA!'
