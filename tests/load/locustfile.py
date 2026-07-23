"""Locust load scenarios for MediaCore API.

Usage:
  uv run locust -f tests/load/locustfile.py --headless -u 10 -r 2 -t 30s --host http://127.0.0.1:8000
"""

from __future__ import annotations

from locust import HttpUser, between, task


class MediaCoreUser(HttpUser):
    wait_time = between(0.1, 0.5)

    def on_start(self) -> None:
        self.headers = {"X-API-Key": "dev-api-key-change-me", "Content-Type": "application/json"}

    @task(5)
    def health(self) -> None:
        self.client.get("/health")

    @task(2)
    def providers(self) -> None:
        self.client.get("/v1/providers", headers=self.headers)

    @task(1)
    def analyze(self) -> None:
        self.client.post(
            "/v1/analyze",
            headers=self.headers,
            json={"url": "https://cdn.example.com/demo.mp4"},
        )
