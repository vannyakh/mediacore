"""Catalog stub for `dailymotion` (overridden at runtime).

Working implementation: ``providers.dailymotion.provider``.
Regenerate stubs with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class DailymotionProvider(StubProvider):
    name = 'dailymotion'
    status = 'not_configured'
    host_suffixes = ('dailymotion.com', 'www.dailymotion.com', 'dai.ly')
    ie_names = ('dailymotion', 'Dailymotion', 'dailymotion:playlist', 'dailymotion:search', 'dailymotion:user')
    source = "catalog"
    description = 'Catalog stub for dailymotion'
