"""Auto-generated MediaCore catalog stub for `rtbf`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RtbfProvider(StubProvider):
    name = 'rtbf'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('RTBF',)
    source = "catalog"
    description = 'Catalog stub for rtbf'
