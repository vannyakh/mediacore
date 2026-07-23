"""Auto-generated MediaCore catalog stub for `srgssrplay`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SrgssrplayProvider(StubProvider):
    name = 'srgssrplay'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('SRGSSRPlay',)
    source = "catalog"
    description = 'srf.ch, rts.ch, rsi.ch, rtr.ch and swissinfo.ch play sites'
