"""Catalog stub for `wikimedia.org` (overridden at runtime).

Working implementation: ``providers.wikimedia.provider``.
Regenerate stubs with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class WikimediaOrgProvider(StubProvider):
    name = 'wikimedia.org'
    status = 'not_configured'
    host_suffixes = ('wikimedia.org',)
    ie_names = ('wikimedia.org',)
    source = "catalog"
    description = 'Catalog stub for wikimedia.org'
