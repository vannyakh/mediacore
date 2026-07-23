"""Auto-generated MediaCore catalog stub for `wnl`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class WnlProvider(StubProvider):
    name = 'wnl'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('wnl',)
    source = "catalog"
    description = 'npo.nl, ntr.nl, omroepwnl.nl, zapp.nl and npo3.nl'
