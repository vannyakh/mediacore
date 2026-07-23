"""Auto-generated MediaCore catalog stub for `rumble`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RumbleProvider(StubProvider):
    name = 'rumble'
    status = 'not_configured'
    host_suffixes = ('rumble.com', 'www.rumble.com')
    ie_names = ('Rumble',)
    source = "catalog"
    description = 'Catalog stub for rumble'
