"""Unit tests for MediaCore CLI (no live server)."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest

from apps.cli import commands
from apps.cli.client import resolve_base, resolve_key, wait_for_job
from apps.cli.main import build_parser, main

pytestmark = pytest.mark.unit


class _FakeResponse:
    def __init__(self, status_code: int = 200, payload: object | None = None, text: str = "") -> None:
        self.status_code = status_code
        self._payload = payload
        self.text = text
        self.content = b"{}" if payload is not None else b""

    @property
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300

    def json(self) -> object:
        return self._payload

    def raise_for_status(self) -> None:
        if not self.is_success:
            raise httpx.HTTPStatusError(
                "error",
                request=httpx.Request("GET", "http://test"),
                response=httpx.Response(self.status_code, text=self.text or "err"),
            )


class _FakeClient:
    def __init__(self, routes: dict[tuple[str, str], _FakeResponse | list[_FakeResponse]]) -> None:
        self.routes = routes
        self.calls: list[tuple[str, str, dict | None]] = []

    def __enter__(self) -> _FakeClient:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def request(self, method: str, path: str, json: dict | None = None) -> _FakeResponse:
        self.calls.append((method, path, json))
        key = (method.upper(), path)
        value = self.routes[key]
        if isinstance(value, list):
            if not value:
                raise AssertionError(f"no more responses for {key}")
            return value.pop(0)
        return value

    def get(self, path: str) -> _FakeResponse:
        return self.request("GET", path)

    def post(self, path: str, json: dict | None = None) -> _FakeResponse:
        return self.request("POST", path, json=json)


def test_parser_requires_command():
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([])


def test_parser_analyze_and_download_wait():
    parser = build_parser()
    args = parser.parse_args(["analyze", "https://example.com/a.mp4"])
    assert args.command == "analyze"
    assert args.url.endswith("a.mp4")

    args = parser.parse_args(
        ["download", "https://example.com/a.mp4", "--format", "720p", "--wait", "--wait-timeout", "30"]
    )
    assert args.wait is True
    assert args.wait_timeout == 30.0
    assert args.format == "720p"


def test_resolve_env_overrides(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("MEDIACORE_BASE", "http://api.example:9000/")
    monkeypatch.setenv("MEDIACORE_API_KEY", "secret-key")
    assert resolve_base(None) == "http://api.example:9000"
    assert resolve_key(None) == "secret-key"
    assert resolve_base("http://cli") == "http://cli"
    assert resolve_key("cli-key") == "cli-key"


def test_cmd_analyze(monkeypatch: pytest.MonkeyPatch):
    client = _FakeClient(
        {
            ("POST", "/v1/analyze"): _FakeResponse(
                payload={"platform": "generic", "title": "demo", "formats": []}
            )
        }
    )
    monkeypatch.setattr(commands, "make_client", lambda *a, **k: client)
    args = SimpleNamespace(base="http://localhost:8000", key="k", url="https://example.com/v.mp4")
    assert commands.cmd_analyze(args) == 0
    assert client.calls[0][0] == "POST"


def test_cmd_download_wait(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    client = _FakeClient(
        {
            ("POST", "/v1/download"): _FakeResponse(
                payload={"job_id": "j1", "status": "queued", "type": "download"}
            ),
            ("GET", "/v1/jobs/j1"): [
                _FakeResponse(payload={"id": "j1", "status": "running"}),
                _FakeResponse(payload={"id": "j1", "status": "completed", "result_url": "/out"}),
            ],
        }
    )
    monkeypatch.setattr(commands, "make_client", lambda *a, **k: client)
    monkeypatch.setattr(commands, "wait_for_job", lambda client, job_id, timeout=120.0: {
        "id": job_id,
        "status": "completed",
        "result_url": "/out",
    })
    args = SimpleNamespace(
        base="http://localhost:8000",
        key="k",
        url="https://example.com/v.mp4",
        format="original",
        wait=True,
        wait_timeout=10.0,
    )
    assert commands.cmd_download(args) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["status"] == "completed"


def test_wait_for_job_polls():
    client = _FakeClient(
        {
            ("GET", "/v1/jobs/abc"): [
                _FakeResponse(payload={"id": "abc", "status": "running"}),
                _FakeResponse(payload={"id": "abc", "status": "completed"}),
            ]
        }
    )
    result = wait_for_job(client, "abc", timeout=5.0, interval=0.01)  # type: ignore[arg-type]
    assert result["status"] == "completed"


def test_cmd_subtitle_path_vs_url(monkeypatch: pytest.MonkeyPatch):
    client = _FakeClient(
        {
            ("POST", "/v1/subtitles"): _FakeResponse(
                payload={"job_id": "s1", "status": "queued", "type": "subtitles"}
            )
        }
    )
    monkeypatch.setattr(commands, "make_client", lambda *a, **k: client)

    args = SimpleNamespace(
        base="http://x",
        key="k",
        file="/tmp/a.mp4",
        url=None,
        wait=False,
        wait_timeout=1.0,
    )
    assert commands.cmd_subtitle(args) == 0
    assert client.calls[-1][2] == {"path": "/tmp/a.mp4"}

    args.url = "https://example.com/v.mp4"
    assert commands.cmd_subtitle(args) == 0
    assert client.calls[-1][2] == {"url": "https://example.com/v.mp4"}


def test_plugin_install_from_external_path(tmp_path: Path, capsys: pytest.CaptureFixture[str]):
    src = tmp_path / "src" / "demo"
    dest_root = tmp_path / "plugins"
    src.mkdir(parents=True)
    dest_root.mkdir()
    (src / "plugin.py").write_text(
        'PLUGIN = {"name": "mediacore-plugin-demo", "kind": "storage", '
        '"status": "available", "capabilities": ["store"]}\n',
        encoding="utf-8",
    )
    args = SimpleNamespace(target=str(src), plugins_root=str(dest_root))
    assert commands.cmd_plugin_install(args) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "installed"
    assert (dest_root / "demo" / "plugin.py").is_file()

    # Second install of same in-tree name reports already installed
    args = SimpleNamespace(target="demo", plugins_root=str(dest_root))
    assert commands.cmd_plugin_install(args) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "already_installed"


def test_plugin_install_missing(tmp_path: Path):
    args = SimpleNamespace(target="does-not-exist", plugins_root=str(tmp_path))
    assert commands.cmd_plugin_install(args) == 1


def test_plugin_list_falls_back_local(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    def boom(*_a, **_k):
        raise httpx.ConnectError("down", request=httpx.Request("GET", "http://x"))

    monkeypatch.setattr(commands, "make_client", boom)
    args = SimpleNamespace(base="http://localhost:8000", key="k")
    assert commands.cmd_plugin_list(args) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["source"] == "local"
    assert payload["count"] >= 1


def test_doctor_reports_checks(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    client = _FakeClient(
        {
            ("GET", "/health"): _FakeResponse(payload={"status": "ok"}),
            ("GET", "/v1/system"): _FakeResponse(payload={"version": "0.1.0", "plugins": 3}),
        }
    )
    monkeypatch.setattr(commands, "make_client", lambda *a, **k: client)
    monkeypatch.setattr(commands, "ffmpeg_available", lambda: True)
    args = SimpleNamespace(base="http://localhost:8000", key="k")
    assert commands.cmd_doctor(args) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["ok"] is True
    assert payload["checks"]["ffmpeg"]["ok"] is True
    assert payload["checks"]["plugins"]["total"] >= 1


def test_main_http_error(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    def boom(_args):
        raise httpx.ConnectError("down", request=httpx.Request("GET", "http://x"))

    monkeypatch.setattr(commands, "cmd_analyze", boom)
    code = main(["analyze", "https://example.com/v.mp4"])
    assert code == 1
    assert "error:" in capsys.readouterr().err
