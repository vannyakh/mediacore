"""Auto-generated MediaCore catalog stub for `fc2`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Fc2Provider(StubProvider):
    name = 'fc2'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('fc2', 'fc2:embed', 'fc2:live')
    source = "catalog"
    description = 'Catalog stub for fc2'
