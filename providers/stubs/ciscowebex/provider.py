"""Auto-generated MediaCore catalog stub for `ciscowebex`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CiscowebexProvider(StubProvider):
    name = 'ciscowebex'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ciscowebex',)
    source = "catalog"
    description = 'Cisco Webex'
