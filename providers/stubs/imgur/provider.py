"""Catalog stub for `imgur` (overridden at runtime).

Working implementation: ``providers.imgur.provider``.
Regenerate stubs with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ImgurProvider(StubProvider):
    name = 'imgur'
    status = 'not_configured'
    host_suffixes = ('imgur.com', 'i.imgur.com', 'www.imgur.com')
    ie_names = ('Imgur', 'imgur:album', 'imgur:gallery')
    source = "catalog"
    description = 'Catalog stub for imgur'
