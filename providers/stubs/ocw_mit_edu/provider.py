"""Auto-generated MediaCore catalog stub for `ocw.mit.edu`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class OcwMitEduProvider(StubProvider):
    name = 'ocw.mit.edu'
    status = 'not_configured'
    host_suffixes = ('ocw.mit.edu',)
    ie_names = ('ocw.mit.edu',)
    source = "catalog"
    description = 'Catalog stub for ocw.mit.edu'
