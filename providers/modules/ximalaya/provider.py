"""Auto-generated MediaCore platform module for `ximalaya`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class XimalayaProvider(PlatformModule):
    name = 'ximalaya'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ximalaya', 'ximalaya:album')
    source = "catalog"
    description = '喜马拉雅FM'
