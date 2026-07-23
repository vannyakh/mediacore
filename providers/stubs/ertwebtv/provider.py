"""Auto-generated MediaCore catalog stub for `ertwebtv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ErtwebtvProvider(StubProvider):
    name = 'ertwebtv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ertwebtv:embed',)
    source = "catalog"
    description = 'ert.gr webtv embedded videos'
