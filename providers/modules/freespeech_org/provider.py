"""Auto-generated MediaCore platform module for `freespeech.org`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class FreespeechOrgProvider(PlatformModule):
    name = 'freespeech.org'
    status = 'not_configured'
    host_suffixes = ('freespeech.org', 'www.freespeech.org')
    ie_names = ('freespeech.org',)
    source = "catalog"
    description = 'Platform module for freespeech.org'
