"""Auto-generated MediaCore catalog stub for `telecaribeplay`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TelecaribeplayProvider(StubProvider):
    name = 'telecaribeplay'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('TelecaribePlay',)
    source = "catalog"
    description = 'Catalog stub for telecaribeplay'
