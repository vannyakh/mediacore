"""Auto-generated MediaCore catalog stub for `brilliantpala`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BrilliantpalaProvider(StubProvider):
    name = 'brilliantpala'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Brilliantpala:Classes', 'Brilliantpala:Elearn')
    source = "catalog"
    description = 'VoD on classes.brilliantpala.org'
