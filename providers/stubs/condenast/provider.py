"""Auto-generated MediaCore catalog stub for `condenast`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CondenastProvider(StubProvider):
    name = 'condenast'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('CondeNast',)
    source = "catalog"
    description = 'Condé Nast media group: Allure, Architectural Digest, Ars Technica, Bon Appétit, Brides, Condé Nast, Condé Nast Traveler, Details, Epicurious, GQ, Glamour, Golf Digest, SELF, Teen Vogue, The New Yorker, Vanity Fair, Vogue, W Magazine, WIRED'
