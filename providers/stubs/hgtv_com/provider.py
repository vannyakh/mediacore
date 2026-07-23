"""Auto-generated MediaCore catalog stub for `hgtv.com`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class HgtvComProvider(StubProvider):
    name = 'hgtv.com'
    status = 'not_configured'
    host_suffixes = ('hgtv.com',)
    ie_names = ('hgtv.com:show',)
    source = "catalog"
    description = 'Catalog stub for hgtv.com'
