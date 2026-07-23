"""Auto-generated MediaCore catalog stub for `dhm`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class DhmProvider(StubProvider):
    name = 'dhm'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('DHM',)
    source = "catalog"
    description = 'Filmarchiv - Deutsches Historisches Museum'
