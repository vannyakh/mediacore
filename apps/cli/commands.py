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
    vprint,
    wait_for_job,
)
from packages.media.wrapper import ffmpeg_available
from packages.plugins.loader import PluginLoader


def _plugins_root() -> Path:
    return Path(__file__).resolve().parents[2] / "plugins"


def _is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _read_batch_file(path: str) -> list[str]:
    text = Path(path).expanduser().read_text(encoding="utf-8")
    urls: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        urls.append(line.split()[0])
    return urls


def _collect_urls(args: argparse.Namespace) -> list[str]:
    urls: list[str] = []
    batch = getattr(args, "batch_file", None)
    if batch:
        urls.extend(_read_batch_file(batch))
    single = getattr(args, "url", None)
    if single:
        urls.append(single)
    for u in getattr(args, "urls", None) or []:
        urls.append(u)
    # dedupe preserve order
    seen: set[str] = set()
    out: list[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def _format_rows(meta: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for fmt in meta.get("formats") or []:
        if not isinstance(fmt, dict):
            continue
        rows.append(
            {
                "id": fmt.get("id") or fmt.get("format_id"),
                "quality": fmt.get("quality"),
                "container": fmt.get("container"),
                "height": fmt.get("height"),
                "width": fmt.get("width"),
            }
        )
    return rows


def _print_formats(meta: dict[str, Any]) -> None:
    platform = meta.get("platform") or "?"
    title = meta.get("title") or ""
    print(f"[{platform}] {title}".rstrip())
    print(f"{'ID':<16} {'QUALITY':<12} {'CONTAINER':<10} {'SIZE'}")
    print("-" * 52)
    for row in _format_rows(meta):
        print(
            f"{str(row.get('id') or '-'):<16} "
            f"{str(row.get('quality') or '-'):<12} "
            f"{str(row.get('container') or '-'):<10} "
            f"{row.get('width') or '-'}x{row.get('height') or '-'}"
        )


def _apply_output_template(template: str, meta: dict[str, Any], url: str) -> Path:
    title = str(meta.get("title") or "media").replace("/", "_").strip() or "media"
    vid = str(meta.get("id") or meta.get("platform") or "file")
    path = template.replace("{title}", title).replace("{id}", vid).replace("{ext}", "mp4")
    if path.endswith(("/", "\\")):
        path = str(Path(path) / f"{title}.mp4")
    return Path(path).expanduser()


def _copy_result_to_output(job: dict[str, Any], meta: dict[str, Any], url: str, output: str) -> str | None:
    src = job.get("result_path")
    if not src:
        return None
    src_path = Path(str(src))
    if not src_path.is_file():
        return None
    dest = _apply_output_template(output, meta, url)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.is_dir():
        dest = dest / src_path.name
    shutil.copy2(src_path, dest)
    return str(dest)


def _maybe_wait(
    client: httpx.Client, body: dict[str, Any], args: argparse.Namespace
) -> dict[str, Any]:
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
    urls = _collect_urls(args)
    if not urls:
        eprint("error: provide a URL")
        return 2
    code = 0
    with make_client(args.base, args.key) as client:
        for url in urls:
            vprint(f"analyze {url}")
            data = request_json(client, "POST", "/v1/analyze", json_body={"url": url})
            if getattr(args, "list_formats", False):
                _print_formats(data if isinstance(data, dict) else {})
            else:
                print_json(data)
            _maybe_hint_not_configured(data if isinstance(data, dict) else {})
    return code


def cmd_download(args: argparse.Namespace) -> int:
    urls = _collect_urls(args)
    if not urls:
        eprint("error: provide a URL or --batch-file")
        return 2
    if getattr(args, "list_formats", False) or getattr(args, "simulate", False):
        args.urls = urls
        args.url = None
        return cmd_analyze(args)

    fmt = getattr(args, "format", "original") or "original"
    output = getattr(args, "output", None)
    exit_code = 0
    with make_client(args.base, args.key) as client:
        for url in urls:
            vprint(f"download {url}")
            meta: dict[str, Any] = {}
            if output:
                try:
                    meta = request_json(client, "POST", "/v1/analyze", json_body={"url": url}) or {}
                except httpx.HTTPError:
                    meta = {}
            data = request_json(
                client,
                "POST",
                "/v1/download",
                json_body={"url": url, "format": fmt},
            )
            data = _maybe_wait(client, data, args)
            if output and isinstance(data, dict) and data.get("status") == "completed":
                copied = _copy_result_to_output(data, meta, url, output)
                if copied:
                    data = {**data, "output_path": copied}
            print_json(data)
            _maybe_hint_not_configured(data if isinstance(data, dict) else {})
            if isinstance(data, dict) and str(data.get("status")) in {"failed", "cancelled"}:
                exit_code = 1
    return exit_code


def cmd_get(args: argparse.Namespace) -> int:
    """URL-first entry (yt-dlp-like UX): -F/-s analyze; else download with --wait."""
    urls = _collect_urls(args)
    if not urls:
        eprint("error: provide URL(s) or -a/--batch-file")
        return 2
    args.urls = urls
    args.url = None
    if getattr(args, "list_formats", False) or getattr(args, "simulate", False):
        return cmd_analyze(args)
    # Default get = download + wait (permitted sources only)
    if not hasattr(args, "wait") or args.wait is None:
        args.wait = True
    args.wait = True
    return cmd_download(args)


def cmd_process(args: argparse.Namespace) -> int:
    """Download (permitted sources) then convert via ffmpeg plugin — not scrape+ffmpeg."""
    container = getattr(args, "container", "mp4") or "mp4"
    wait_timeout = float(getattr(args, "wait_timeout", 120.0))
    with make_client(args.base, args.key) as client:
        download_job = request_json(
            client,
            "POST",
            "/v1/download",
            json_body={"url": args.url, "format": args.format},
        )
        # Always wait for download so we can chain convert
        wait_ns = argparse.Namespace(wait=True, wait_timeout=wait_timeout)
        download_job = _maybe_wait(client, download_job, wait_ns)
        if str(download_job.get("status")) != "completed":
            print_json({"step": "download", "job": download_job})
            _maybe_hint_not_configured(download_job)
            eprint(
                "hint: process needs a completed permitted download, then ffmpeg convert. "
                "Check: mediacore doctor"
            )
            return 1
        local_path = download_job.get("result_path")
        if not local_path:
            print_json({"step": "download", "job": download_job})
            eprint("error: download completed without result_path (cannot chain convert)")
            return 1
        convert_job = request_json(
            client,
            "POST",
            "/v1/convert",
            json_body={"path": local_path, "options": {"container": container}},
        )
        convert_job = _maybe_wait(client, convert_job, wait_ns)
        print_json(
            {
                "pipeline": "download→convert",
                "note": "Uses permitted download + ffmpeg plugin; not watch-page scrape.",
                "download": download_job,
                "convert": convert_job,
            }
        )
        if str(convert_job.get("status")) != "completed":
            eprint("hint: convert failed — is ffmpeg installed? Try: mediacore doctor")
            return 1
    return 0


def _maybe_hint_not_configured(data: Any) -> None:
    if not isinstance(data, dict):
        return
    code = data.get("code")
    nested = data.get("error")
    if isinstance(nested, dict):
        code = code or nested.get("code")
        err = str(nested.get("message") or nested.get("error") or nested)
    else:
        err = str(nested or data.get("message") or "")
    status = str(data.get("status") or "")
    if code == "provider_not_configured" or "provider_not_configured" in err or (
        status == "failed" and "not configured" in err.lower()
    ):
        platform = data.get("platform") or data.get("provider") or "this platform"
        eprint(
            f"hint: detected {platform} — page download needs a permitted API; "
            "direct media on known hosts may work. "
            "Try: mediacore -s URL  |  mediacore providers list --download-only"
        )


_DOWNLOAD_STATUSES = frozenset({"active", "available"})
_METADATA_STATUSES = frozenset({"metadata_only", "metadata"})
_WORKING_STATUSES = _DOWNLOAD_STATUSES | _METADATA_STATUSES | frozenset({"example"})


def _provider_capability(status: str) -> str:
    s = status.lower()
    if s in _DOWNLOAD_STATUSES:
        return "download"
    if s in _METADATA_STATUSES:
        return "metadata"
    if s == "example":
        return "example"
    return "catalog"


def cmd_providers_list(args: argparse.Namespace) -> int:
    status_filter = getattr(args, "status", None)
    download_only = bool(getattr(args, "download_only", False))
    try:
        with make_client(args.base, args.key) as client:
            providers = request_json(client, "GET", "/v1/providers")
            catalog = request_json(client, "GET", "/v1/providers/catalog")
            source = "api"
    except httpx.HTTPError:
        from packages.registry.providers import get_registry
        from providers.catalog import catalog_summary

        registry = get_registry()
        providers = registry.platforms()
        catalog = catalog_summary()
        source = "local"

    rows = list(providers or [])
    if status_filter:
        wanted = status_filter.lower()
        rows = [p for p in rows if str(p.get("status", "")).lower() == wanted]
    if download_only:
        rows = [p for p in rows if str(p.get("status", "")).lower() in _DOWNLOAD_STATUSES]

    working = [
        p
        for p in (providers or [])
        if str(p.get("status", "")) in _WORKING_STATUSES
    ]
    by_status: dict[str, int] = {}
    for p in providers or []:
        key = str(p.get("status") or "unknown")
        by_status[key] = by_status.get(key, 0) + 1

    listed = rows if (status_filter or download_only) else working
    download_providers = [
        {**p, "capability": "download"}
        for p in listed
        if str(p.get("status", "")).lower() in _DOWNLOAD_STATUSES
    ]
    metadata_providers = [
        {**p, "capability": "metadata"}
        for p in listed
        if str(p.get("status", "")).lower() in _METADATA_STATUSES
    ]
    other_providers = [
        {**p, "capability": _provider_capability(str(p.get("status", "")))}
        for p in listed
        if str(p.get("status", "")).lower()
        not in _DOWNLOAD_STATUSES | _METADATA_STATUSES
    ]

    print_json(
        {
            "source": source,
            "working_count": len(working),
            "listed": len(listed),
            "status_filter": status_filter,
            "download_only": download_only,
            "by_status": by_status,
            "by_capability": {
                "download": len(download_providers),
                "metadata": len(metadata_providers),
                "other": len(other_providers),
            },
            "catalog": catalog,
            "download": download_providers,
            "metadata": metadata_providers,
            "other": other_providers,
            "providers": [
                {**p, "capability": _provider_capability(str(p.get("status", "")))}
                for p in listed
            ],
            "note": (
                "active/available = permitted download; metadata_only = analyze only; "
                "catalog modules detect hosts (direct media may still download). "
                "Filter: --download-only  |  search: mediacore providers search QUERY"
            ),
        }
    )
    return 0


def cmd_providers_search(args: argparse.Namespace) -> int:
    query = args.query
    limit = int(getattr(args, "limit", 50) or 50)
    try:
        with make_client(args.base, args.key) as client:
            hits = request_json(
                client,
                "GET",
                "/v1/providers/catalog/search",
                params={"q": query, "limit": limit},
            )
            source = "api"
    except httpx.HTTPError:
        from providers.catalog import search_extractors

        hits = search_extractors(query, limit=limit)
        source = "local"
    print_json({"source": source, "query": query, "count": len(hits or []), "results": hits})
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
        f"plugin not found: {target!r} "
        f"(expected a directory with plugin.py or a name under {plugins_root})"
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

    try:
        from packages.config.settings import get_settings

        settings = get_settings()
        report["checks"]["events_redis"] = {
            "ok": True,
            "enabled": bool(settings.events_redis_enabled),
            "note": (
                "Redis optional locally when EVENTS_REDIS_ENABLED=false "
                "(default). Enable for multi-process event fan-out."
            ),
        }
    except Exception as exc:  # noqa: BLE001
        report["checks"]["events_redis"] = {"ok": True, "warning": str(exc)}

    print_json(report)
    return 0 if report["ok"] else 1


def cmd_worker(_args: argparse.Namespace) -> int:
    from apps.worker.main import run

    run()
    return 0
