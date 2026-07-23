"""Auto-generated MediaCore catalog stub for `life`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class LifeProvider(StubProvider):
    name = 'life'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('life', 'life:embed')
    source = "catalog"
    description = 'Life.ru'
