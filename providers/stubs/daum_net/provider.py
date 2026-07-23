"""Auto-generated MediaCore catalog stub for `daum.net`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class DaumNetProvider(StubProvider):
    name = 'daum.net'
    status = 'not_configured'
    host_suffixes = ('daum.net',)
    ie_names = ('daum.net', 'daum.net:clip', 'daum.net:playlist', 'daum.net:user')
    source = "catalog"
    description = 'Catalog stub for daum.net'
