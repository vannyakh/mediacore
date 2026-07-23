"""Catalog stub for `bandcamp` (overridden at runtime).

Working implementation: ``providers.bandcamp.provider``.
Regenerate stubs with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BandcampProvider(StubProvider):
    name = 'bandcamp'
    status = 'not_configured'
    host_suffixes = ('bandcamp.com',)
    ie_names = ('Bandcamp', 'Bandcamp:album', 'Bandcamp:user', 'Bandcamp:weekly')
    source = "catalog"
    description = 'Catalog stub for bandcamp'
