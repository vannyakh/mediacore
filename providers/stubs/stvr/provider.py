"""Auto-generated MediaCore catalog stub for `stvr`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class StvrProvider(StubProvider):
    name = 'stvr'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('stvr',)
    source = "catalog"
    description = 'Slovak Television and Radio (formerly RTVS)'
