"""Auto-generated MediaCore catalog stub for `bt`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BtProvider(StubProvider):
    name = 'bt'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('bt:article', 'bt:vestlendingen')
    source = "catalog"
    description = 'Bergens Tidende Articles'
