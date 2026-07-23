"""Auto-generated MediaCore catalog stub for `lemonde`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class LemondeProvider(StubProvider):
    name = 'lemonde'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Lemonde',)
    source = "catalog"
    description = 'Catalog stub for lemonde'
