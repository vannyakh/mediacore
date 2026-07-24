"""Auto-generated MediaCore platform module for `cnn`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class CnnProvider(PlatformModule):
    name = 'cnn'
    status = 'not_configured'
    host_suffixes = ('cnn.com', 'www.cnn.com', 'edition.cnn.com', 'money.cnn.com', 'cnnespanol.cnn.com')
    ie_names = ('CNN', 'cnn')
    source = "catalog"
    description = 'Platform module for cnn'
