"""Auto-generated MediaCore platform module for `digitallyspeaking`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class DigitallyspeakingProvider(PlatformModule):
    name = 'digitallyspeaking'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('DigitallySpeaking',)
    source = "catalog"
    description = 'Platform module for digitallyspeaking'
