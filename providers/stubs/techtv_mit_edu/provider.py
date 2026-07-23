"""Auto-generated MediaCore catalog stub for `techtv.mit.edu`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TechtvMitEduProvider(StubProvider):
    name = 'techtv.mit.edu'
    status = 'not_configured'
    host_suffixes = ('techtv.mit.edu',)
    ie_names = ('techtv.mit.edu',)
    source = "catalog"
    description = 'Catalog stub for techtv.mit.edu'
