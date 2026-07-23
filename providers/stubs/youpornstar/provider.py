"""Auto-generated MediaCore catalog stub for `youpornstar`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class YoupornstarProvider(StubProvider):
    name = 'youpornstar'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('YouPornStar',)
    source = "catalog"
    description = 'YouPorn Pornstar, with description, sorting and pagination'
