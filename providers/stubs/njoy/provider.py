"""Auto-generated MediaCore catalog stub for `njoy`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NjoyProvider(StubProvider):
    name = 'njoy'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('njoy', 'njoy:embed')
    source = "catalog"
    description = 'N-JOY'
