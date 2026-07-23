"""Auto-generated MediaCore catalog stub for `cnn`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CnnProvider(StubProvider):
    name = 'cnn'
    status = 'not_configured'
    host_suffixes = ('cnn.com', 'www.cnn.com')
    ie_names = ('CNN',)
    source = "catalog"
    description = 'Catalog stub for cnn'
