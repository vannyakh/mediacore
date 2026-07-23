"""Auto-generated MediaCore catalog stub for `rte`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RteProvider(StubProvider):
    name = 'rte'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('rte', 'rte:radio')
    source = "catalog"
    description = 'Raidió Teilifís Éireann TV'
