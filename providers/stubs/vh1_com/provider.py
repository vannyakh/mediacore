"""Auto-generated MediaCore catalog stub for `vh1.com`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Vh1ComProvider(StubProvider):
    name = 'vh1.com'
    status = 'not_configured'
    host_suffixes = ('vh1.com',)
    ie_names = ('vh1.com',)
    source = "catalog"
    description = 'Catalog stub for vh1.com'
