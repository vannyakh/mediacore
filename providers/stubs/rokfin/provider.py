"""Auto-generated MediaCore catalog stub for `rokfin`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RokfinProvider(StubProvider):
    name = 'rokfin'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Rokfin', 'rokfin:channel', 'rokfin:search', 'rokfin:stack')
    source = "catalog"
    description = 'Rokfin Channels'
