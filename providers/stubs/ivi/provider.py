"""Auto-generated MediaCore catalog stub for `ivi`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class IviProvider(StubProvider):
    name = 'ivi'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ivi', 'ivi:compilation')
    source = "catalog"
    description = 'ivi.ru'
