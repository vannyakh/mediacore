"""Auto-generated MediaCore catalog stub for `cam4`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Cam4Provider(StubProvider):
    name = 'cam4'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('CAM4',)
    source = "catalog"
    description = 'Catalog stub for cam4'
