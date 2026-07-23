"""Auto-generated MediaCore catalog stub for `canalc2.tv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Canalc2TvProvider(StubProvider):
    name = 'canalc2.tv'
    status = 'not_configured'
    host_suffixes = ('canalc2.tv',)
    ie_names = ('canalc2.tv',)
    source = "catalog"
    description = 'Catalog stub for canalc2.tv'
