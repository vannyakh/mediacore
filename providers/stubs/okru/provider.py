"""Auto-generated MediaCore catalog stub for `okru`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class OkruProvider(StubProvider):
    name = 'okru'
    status = 'not_configured'
    host_suffixes = ('ok.ru', 'www.ok.ru')
    ie_names = ('Odnoklassniki',)
    source = "catalog"
    description = 'Catalog stub for okru'
