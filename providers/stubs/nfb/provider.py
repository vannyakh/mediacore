"""Auto-generated MediaCore catalog stub for `nfb`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NfbProvider(StubProvider):
    name = 'nfb'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('nfb', 'nfb:series')
    source = "catalog"
    description = 'nfb.ca and onf.ca films and episodes'
