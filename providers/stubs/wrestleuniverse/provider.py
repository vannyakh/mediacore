"""Auto-generated MediaCore catalog stub for `wrestleuniverse`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class WrestleuniverseProvider(StubProvider):
    name = 'wrestleuniverse'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('wrestleuniverse:ppv', 'wrestleuniverse:vod')
    source = "catalog"
    description = 'Catalog stub for wrestleuniverse'
