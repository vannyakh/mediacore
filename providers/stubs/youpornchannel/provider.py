"""Auto-generated MediaCore catalog stub for `youpornchannel`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class YoupornchannelProvider(StubProvider):
    name = 'youpornchannel'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('YouPornChannel',)
    source = "catalog"
    description = 'YouPorn channel, with sorting and pagination'
