"""Auto-generated MediaCore catalog stub for `phoenix.de`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PhoenixDeProvider(StubProvider):
    name = 'phoenix.de'
    status = 'not_configured'
    host_suffixes = ('phoenix.de',)
    ie_names = ('phoenix.de',)
    source = "catalog"
    description = 'Catalog stub for phoenix.de'
