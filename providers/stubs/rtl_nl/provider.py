"""Auto-generated MediaCore catalog stub for `rtl.nl`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RtlNlProvider(StubProvider):
    name = 'rtl.nl'
    status = 'not_configured'
    host_suffixes = ('rtl.nl',)
    ie_names = ('rtl.nl',)
    source = "catalog"
    description = 'rtl.nl and rtlxl.nl'
