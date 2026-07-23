"""Auto-generated MediaCore catalog stub for `megatvcom`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MegatvcomProvider(StubProvider):
    name = 'megatvcom'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('megatvcom', 'megatvcom:embed')
    source = "catalog"
    description = 'megatv.com videos'
