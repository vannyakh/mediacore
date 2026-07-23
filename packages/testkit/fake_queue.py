"""Fake queue that records enqueue calls without Dramatiq/Redis."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class FakeQueue:
    downloads: list[str] = field(default_factory=list)
    cleanups: list[str] = field(default_factory=list)
    analyzes: list[str] = field(default_factory=list)
    processes: list[tuple[str, str]] = field(default_factory=list)

    def enqueue_download(self, job_id: str) -> None:
        self.downloads.append(job_id)

    def enqueue_cleanup(self, job_id: str) -> None:
        self.cleanups.append(job_id)

    def enqueue_analyze(self, job_id: str) -> None:
        self.analyzes.append(job_id)

    def enqueue_process(self, job_id: str, operation: str) -> None:
        self.processes.append((job_id, operation))
