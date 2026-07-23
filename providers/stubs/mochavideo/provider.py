"""Auto-generated MediaCore catalog stub for `mochavideo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MochavideoProvider(StubProvider):
    name = 'mochavideo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('MochaVideo',)
    source = "catalog"
    description = 'Catalog stub for mochavideo'
