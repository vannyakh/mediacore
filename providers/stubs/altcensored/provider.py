"""Auto-generated MediaCore catalog stub for `altcensored`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class AltcensoredProvider(StubProvider):
    name = 'altcensored'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('altcensored', 'altcensored:channel')
    source = "catalog"
    description = 'Catalog stub for altcensored'
