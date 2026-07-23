"""Browser automation stub — prefer packages for future Playwright integration."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BrowserSessionConfig:
    headless: bool = True
    timeout_ms: int = 30_000


class BrowserSession:
    def __init__(self, config: BrowserSessionConfig | None = None) -> None:
        self.config = config or BrowserSessionConfig()

    @property
    def available(self) -> bool:
        return False
