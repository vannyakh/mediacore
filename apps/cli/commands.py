"""MediaCore CLI command handlers."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx

from apps.cli.client import (
    eprint,
    format_http_error,
    make_client,
    print_json,
    request_json,
    wait_for_job,
)
from packages.media.wrapper import ffmpeg_available
from packages.plugins.loader import PluginLoader


def _plugins_root() -> Path:
    return Path(__file__).resolve().parents[2] / "plugins"


def _is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _maybe_wait(client: httpx.Client, body: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    if not getattr(args, "wait", False):
        return body
    job_id = body.get("job_id") or body.get("id")
    if not job_id:
        return body
    timeout = float(getattr(args, "wait_timeout", 120.0))
    return wait_for_job(client, str(job_id), timeout=timeout)


def cmd_events(args: argparse.Namespace) -> int:
    """List recent events or follow the SSE stream."""
    params: dict[str, Any] = {}
    if args.job_id:
        params["job_id"] = args.job_id
    if not args.follow:
        params["limit"] = args.limit
        with make_client(args.base, args.key) as client:
            data = client.get("/v1/events", params=params)
            data.raise_for_status()
            print_json(data.json())
        return 0

    query = "&".join(f"{k}={v}" for k, v in params.items())
    path = "/v1/events/stream" + (f"?{query}" if query else "")
    with make_client(args.base, args.key, timeout=300.0) as client:
        with client.stream("GET", path) as response:
            response.raise_for_status()
            event_name = "message"
            data_lines: list[str] = []
            for line in response.iter_lines():
                if line.startswith("event:"):
                    event_name = line.split(":", 1)[1].strip()
                elif line.startswith("data:"):
                    data_lines.append(line.split(":", 1)[1].strip())
                elif line.startswith(":"):
                    continue
                elif line == "":
                    if data_lines:
                        payload = "\n".join(data_lines)
                        print(f"{event_name}\t{payload}", flush=True)
                    event_name = "message"
                    data_lines = []
    return 0


def cmd_analyze(args: argparse.Namespace) -> int:
    with make_client(args.base, args.key) as client:
        data = request_json(client, "POST", "/v1/analyze", json_body={"url": args.url})
        print_json(data)
    return 0


def cmd_download(args: argparse.Namespace) -> int:
    with make_client(args.base, args.key) as client:
        data = request_json(
            client,
            "POST",
            "/v1/download",
            json_body={"url": args.url, "format": args.format},
        )
        data = _maybe_wait(client, data, args)
        print_json(data)
    return 0


def cmd_convert(args: argparse.Namespace) -> int:
    with make_client(args.base, args.key) as client:
        data = request_json(
            client,
            "POST",
            "/v1/convert",
            json_body={"path": args.file, "options": {"container": args.container}},
        )
        data = _maybe_wait(client, data, args)
        print_json(data)
    return 0


def cmd_subtitle(args: argparse.Namespace) -> int:
    target = args.url or args.file
    if not target:
        eprint("error: provide a file path or --url")
        return 2
    body: dict[str, Any]
    if args.url or _is_url(target):
        body = {"url": target}
    else:
        body = {"path": target}
    with make_client(args.base, args.key) as client:
        data = request_json(client, "POST", "/v1/subtitles", json_body=body)
        data = _maybe_wait(client, data, args)
        print_json(data)
    return 0


def cmd_plugin_list(args: argparse.Namespace) -> int:
    try:
        with make_client(args.base, args.key) as client:
            plugins = request_json(client, "GET", "/v1/plugins")
            source = "api"
    except httpx.HTTPError:
        plugins = [p.to_dict() for p in PluginLoader(root=_plugins_root()).discover()]
        source = "local"
    by_kind: dict[str, list[Any]] = {}
    for plugin in plugins or []:
        by_kind.setdefault(plugin.get("kind", "unknown"), []).append(plugin)
    print_json({"source": source, "count": len(plugins or []), "by_kind": by_kind})
    return 0


def _normalize_plugin_dir_name(name: str) -> str:
    value = name.strip().rstrip("/")
    if value.startswith("mediacore-plugin-"):
        value = value.removeprefix("mediacore-plugin-")
    return value


def _resolve_install_source(target: str, plugins_root: Path) -> Path:
    path = Path(target).expanduser().resolve()
    if path.is_dir() and (path / "plugin.py").exists():
        return path

    name = _normalize_plugin_dir_name(target)
    candidate = (plugins_root / name).resolve()
    if candidate.is_dir() and (candidate / "plugin.py").exists():
        return candidate

    # Also allow matching by PLUGIN name via discovery
    loader = PluginLoader(root=plugins_root)
    for info in loader.discover():
        if info.name == target or info.name == f"mediacore-plugin-{name}":
            if info.path:
                return Path(info.path)
    raise FileNotFoundError(
        f"plugin not found: {target!r} (expected a directory with plugin.py or a name under {plugins_root})"
    )


def _validate_plugin_dir(source: Path) -> dict[str, Any]:
    source = source.resolve()
    if not (source / "plugin.py").is_file():
        raise ValueError(f"missing plugin.py in {source}")
    loader = PluginLoader(root=source.parent)
    infos = loader.discover()
    match = next((p for p in infos if Path(p.path or "").resolve() == source), None)
    if match is None:
        match = next((p for p in infos if Path(p.path or "").name == source.name), None)
    if match is None:
        raise ValueError(f"could not load plugin manifest from {source}")
    if match.status == "error":
        raise ValueError(match.description or "plugin manifest error")
    return match.to_dict()


def cmd_plugin_install(args: argparse.Namespace) -> int:
    plugins_root = Path(getattr(args, "plugins_root", None) or _plugins_root())
    plugins_root.mkdir(parents=True, exist_ok=True)
    try:
        source = _resolve_install_source(args.target, plugins_root)
        info = _validate_plugin_dir(source)
    except (FileNotFoundError, ValueError) as exc:
        eprint(f"error: {exc}")
        return 1

    dest_name = source.name
    dest = (plugins_root / dest_name).resolve()
    source_resolved = source.resolve()

    if source_resolved == dest or source_resolved.is_relative_to(plugins_root.resolve()):
        print_json(
            {
                "status": "already_installed",
                "name": info.get("name"),
                "path": str(source_resolved),
                "plugin": info,
            }
        )
        return 0

    if dest.exists():
        eprint(f"error: destination already exists: {dest}")
        return 1

    shutil.copytree(source_resolved, dest)
    installed = _validate_plugin_dir(dest)
    print_json(
        {
            "status": "installed",
            "name": installed.get("name"),
            "path": str(dest),
            "plugin": installed,
        }
    )
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    report: dict[str, Any] = {"ok": True, "checks": {}}

    # API health / system
    try:
        with make_client(args.base, args.key) as client:
            health_res = client.get("/health")
            system_res = client.get("/v1/system")
            report["checks"]["api_health"] = {
                "ok": health_res.is_success,
                "status_code": health_res.status_code,
                "body": health_res.json() if health_res.content else None,
            }
            report["checks"]["api_system"] = {
                "ok": system_res.is_success,
                "status_code": system_res.status_code,
                "body": system_res.json() if system_res.is_success and system_res.content else None,
            }
            if not (health_res.is_success and system_res.is_success):
                report["ok"] = False
    except httpx.HTTPError as exc:
        report["ok"] = False
        report["checks"]["api_health"] = {"ok": False, "error": format_http_error(exc)}
        report["checks"]["api_system"] = {"ok": False, "error": format_http_error(exc)}

    plugins = PluginLoader(root=_plugins_root()).discover()
    available = sum(1 for p in plugins if p.status == "available")
    report["checks"]["plugins"] = {
        "ok": True,
        "total": len(plugins),
        "available": available,
        "stub": sum(1 for p in plugins if p.status == "stub"),
        "error": sum(1 for p in plugins if p.status == "error"),
    }

    ff_ok = ffmpeg_available()
    report["checks"]["ffmpeg"] = {"ok": ff_ok, "available": ff_ok}
    if not ff_ok:
        # ffmpeg missing is a warning for doctor, not a hard failure of the platform
        report["checks"]["ffmpeg"]["warning"] = "ffmpeg not found on PATH"

    print_json(report)
    return 0 if report["ok"] else 1


def cmd_worker(_args: argparse.Namespace) -> int:
    from apps.worker.main import run

    run()
    return 0
