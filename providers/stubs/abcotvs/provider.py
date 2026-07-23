"""Auto-generated MediaCore catalog stub for `abcotvs`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class AbcotvsProvider(StubProvider):
    name = 'abcotvs'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('abcotvs', 'abcotvs:clips')
    source = "catalog"
    description = 'ABC Owned Television Stations'
