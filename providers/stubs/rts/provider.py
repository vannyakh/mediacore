"""Auto-generated MediaCore catalog stub for `rts`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RtsProvider(StubProvider):
    name = 'rts'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('RTS',)
    source = "catalog"
    description = 'RTS.ch'
