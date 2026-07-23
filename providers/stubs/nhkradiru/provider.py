"""Auto-generated MediaCore catalog stub for `nhkradiru`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NhkradiruProvider(StubProvider):
    name = 'nhkradiru'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('NhkRadiru',)
    source = "catalog"
    description = 'NHK らじる (Radiru/Rajiru)'
