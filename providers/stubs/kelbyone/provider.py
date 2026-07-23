"""Auto-generated MediaCore catalog stub for `kelbyone`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class KelbyoneProvider(StubProvider):
    name = 'kelbyone'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('KelbyOne',)
    source = "catalog"
    description = 'Catalog stub for kelbyone'
