"""Auto-generated MediaCore catalog stub for `southpark.cc.com`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SouthparkCcComProvider(StubProvider):
    name = 'southpark.cc.com'
    status = 'not_configured'
    host_suffixes = ('southpark.cc.com',)
    ie_names = ('southpark.cc.com', 'southpark.cc.com:español')
    source = "catalog"
    description = 'Catalog stub for southpark.cc.com'
