"""Auto-generated MediaCore catalog stub for `canalplus`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CanalplusProvider(StubProvider):
    name = 'canalplus'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Canalplus',)
    source = "catalog"
    description = 'mycanal.fr and piwiplus.fr'
