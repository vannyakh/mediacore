"""Auto-generated MediaCore catalog stub for `ndr`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NdrProvider(StubProvider):
    name = 'ndr'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ndr', 'ndr:embed', 'ndr:\u200bembed:base')
    source = "catalog"
    description = 'NDR.de - Norddeutscher Rundfunk'
