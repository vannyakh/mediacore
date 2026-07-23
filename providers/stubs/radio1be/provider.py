"""Auto-generated MediaCore catalog stub for `radio1be`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Radio1beProvider(StubProvider):
    name = 'radio1be'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Radio1Be',)
    source = "catalog"
    description = 'Catalog stub for radio1be'
