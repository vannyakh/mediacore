"""Thread-local download progress callbacks."""

from __future__ import annotations

import threading
from collections.abc import Callable

ProgressCallback = Callable[[int, int | None], None]

_progress_local = threading.local()


def set_progress_callback(callback: ProgressCallback | None) -> None:
    """Thread-local progress hook used by engine during downloads."""
    _progress_local.callback = callback


def get_progress_callback() -> ProgressCallback | None:
    return getattr(_progress_local, "callback", None)
