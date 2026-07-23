"""Catalog stub for `mixcloud` (overridden at runtime).

Working implementation: ``providers.mixcloud.provider``.
Regenerate stubs with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MixcloudProvider(StubProvider):
    name = 'mixcloud'
    status = 'not_configured'
    host_suffixes = ('mixcloud.com', 'www.mixcloud.com')
    ie_names = ('mixcloud', 'Mixcloud', 'mixcloud:playlist', 'mixcloud:user')
    source = "catalog"
    description = 'Catalog stub for mixcloud'
