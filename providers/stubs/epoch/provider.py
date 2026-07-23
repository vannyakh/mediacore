"""Auto-generated MediaCore catalog stub for `epoch`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class EpochProvider(StubProvider):
    name = 'epoch'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Epoch',)
    source = "catalog"
    description = 'Catalog stub for epoch'
