"""Auto-generated MediaCore catalog stub for `jtbc`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class JtbcProvider(StubProvider):
    name = 'jtbc'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('JTBC', 'JTBC:program')
    source = "catalog"
    description = 'jtbc.co.kr'
