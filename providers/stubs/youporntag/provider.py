"""Auto-generated MediaCore catalog stub for `youporntag`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class YouporntagProvider(StubProvider):
    name = 'youporntag'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('YouPornTag',)
    source = "catalog"
    description = 'YouPorn tag (porntags), with sorting, filtering and pagination'
