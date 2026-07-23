"""Auto-generated MediaCore catalog stub for `html5`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Html5Provider(StubProvider):
    name = 'html5'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('html5',)
    source = "catalog"
    description = 'Catalog stub for html5'
