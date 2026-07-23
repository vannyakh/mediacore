"""Catalog stub for `ted` (overridden at runtime).

Working implementation: ``providers.ted.provider``.
Regenerate stubs with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TedProvider(StubProvider):
    name = 'ted'
    status = 'not_configured'
    host_suffixes = ('ted.com', 'www.ted.com')
    ie_names = ('TED',)
    source = "catalog"
    description = 'Catalog stub for ted'
