"""Auto-generated MediaCore catalog stub for `odysee`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class OdyseeProvider(StubProvider):
    name = 'odysee'
    status = 'not_configured'
    host_suffixes = ('odysee.com', 'www.odysee.com')
    ie_names = ('lbry', 'Odysee', 'lbry:channel', 'lbry:playlist')
    source = "catalog"
    description = 'odysee.com'
