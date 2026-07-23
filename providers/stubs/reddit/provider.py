"""Catalog stub for `reddit` (overridden at runtime).

Working implementation: ``providers.reddit.provider``.
Regenerate stubs with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RedditProvider(StubProvider):
    name = 'reddit'
    status = 'not_configured'
    host_suffixes = ('reddit.com', 'www.reddit.com', 'old.reddit.com', 'v.redd.it', 'i.redd.it')
    ie_names = ('Reddit',)
    source = "catalog"
    description = 'Catalog stub for reddit'
