"""Auto-generated MediaCore catalog stub for `zoom`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ZoomProvider(StubProvider):
    name = 'zoom'
    status = 'not_configured'
    host_suffixes = ('zoom.us', 'www.zoom.us')
    ie_names = ('zoom', 'Zoom', 'zoom:clips')
    source = "catalog"
    description = 'Catalog stub for zoom'
