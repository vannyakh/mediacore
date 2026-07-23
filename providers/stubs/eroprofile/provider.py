"""Auto-generated MediaCore catalog stub for `eroprofile`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class EroprofileProvider(StubProvider):
    name = 'eroprofile'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('EroProfile', 'EroProfile:album')
    source = "catalog"
    description = 'Catalog stub for eroprofile'
