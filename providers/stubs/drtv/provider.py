"""Auto-generated MediaCore catalog stub for `drtv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class DrtvProvider(StubProvider):
    name = 'drtv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('drtv', 'drtv:live', 'drtv:season', 'drtv:series')
    source = "catalog"
    description = 'Catalog stub for drtv'
