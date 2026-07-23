"""Auto-generated MediaCore catalog stub for `on24`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class On24Provider(StubProvider):
    name = 'on24'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('on24',)
    source = "catalog"
    description = 'ON24'
