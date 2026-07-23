"""Auto-generated MediaCore catalog stub for `npo.nl`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NpoNlProvider(StubProvider):
    name = 'npo.nl'
    status = 'not_configured'
    host_suffixes = ('npo.nl',)
    ie_names = ('npo.nl:live', 'npo.nl:radio', 'npo.nl:\u200bradio:fragment')
    source = "catalog"
    description = 'Catalog stub for npo.nl'
