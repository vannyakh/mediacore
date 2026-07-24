"""Auto-generated MediaCore platform module for `zoom`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class ZoomProvider(PlatformModule):
    name = 'zoom'
    status = 'not_configured'
    host_suffixes = ('zoom.us', 'www.zoom.us')
    ie_names = ('zoom', 'Zoom', 'zoom:clips')
    source = "catalog"
    description = 'Platform module for zoom'
