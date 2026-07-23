"""Auto-generated MediaCore catalog stub for `muenchentv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MuenchentvProvider(StubProvider):
    name = 'muenchentv'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('MuenchenTV',)
    source = "catalog"
    description = 'münchen.tv'
