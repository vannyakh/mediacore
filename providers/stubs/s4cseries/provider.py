"""Auto-generated MediaCore catalog stub for `s4cseries`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class S4cseriesProvider(StubProvider):
    name = 's4cseries'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('S4CSeries',)
    source = "catalog"
    description = 'Catalog stub for s4cseries'
