"""Auto-generated MediaCore platform module for `condenast`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class CondenastProvider(PlatformModule):
    name = 'condenast'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('CondeNast',)
    source = "catalog"
    description = 'Condé Nast media group: Allure, Architectural Digest, Ars Technica, Bon Appétit, Brides, Condé Nast, Condé Nast Traveler, Details, Epicurious, GQ, Glamour, Golf Digest, SELF, Teen Vogue, The New Yorker, Vanity Fair, Vogue, W Magazine, WIRED'
