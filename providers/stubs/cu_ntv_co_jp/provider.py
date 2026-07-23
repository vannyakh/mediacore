"""Auto-generated MediaCore catalog stub for `cu.ntv.co.jp`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CuNtvCoJpProvider(StubProvider):
    name = 'cu.ntv.co.jp'
    status = 'not_configured'
    host_suffixes = ('cu.ntv.co.jp',)
    ie_names = ('cu.ntv.co.jp',)
    source = "catalog"
    description = '日テレ無料TADA!'
