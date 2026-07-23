"""Auto-generated MediaCore catalog stub for `audius`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class AudiusProvider(StubProvider):
    name = 'audius'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Audius', 'audius:artist', 'audius:playlist', 'audius:track')
    source = "catalog"
    description = 'Audius.co'
