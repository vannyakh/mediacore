"""Auto-generated MediaCore catalog stub for `funk`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class FunkProvider(StubProvider):
    name = 'funk'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Funk',)
    source = "catalog"
    description = 'Catalog stub for funk'
