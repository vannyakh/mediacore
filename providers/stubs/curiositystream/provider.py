"""Auto-generated MediaCore catalog stub for `curiositystream`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CuriositystreamProvider(StubProvider):
    name = 'curiositystream'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('curiositystream', 'curiositystream:collections', 'curiositystream:series')
    source = "catalog"
    description = 'Catalog stub for curiositystream'
