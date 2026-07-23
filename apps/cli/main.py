"""MediaCore CLI."""

from __future__ import annotations

import argparse
import json
import sys

import httpx

DEFAULT_BASE = "http://localhost:8000"
DEFAULT_KEY = "dev-api-key-change-me"


def _client(base: str, key: str) -> httpx.Client:
    return httpx.Client(base_url=base, headers={"X-API-Key": key}, timeout=60.0)


def cmd_analyze(args: argparse.Namespace) -> int:
    with _client(args.base, args.key) as client:
        res = client.post("/v1/analyze", json={"url": args.url})
        res.raise_for_status()
        print(json.dumps(res.json(), indent=2))
    return 0


def cmd_download(args: argparse.Namespace) -> int:
    with _client(args.base, args.key) as client:
        res = client.post("/v1/download", json={"url": args.url, "format": args.format})
        res.raise_for_status()
        print(json.dumps(res.json(), indent=2))
    return 0


def cmd_convert(args: argparse.Namespace) -> int:
    with _client(args.base, args.key) as client:
        res = client.post(
            "/v1/convert",
            json={"path": args.file, "options": {"container": args.container}},
        )
        res.raise_for_status()
        print(json.dumps(res.json(), indent=2))
    return 0


def cmd_subtitle(args: argparse.Namespace) -> int:
    with _client(args.base, args.key) as client:
        res = client.post("/v1/subtitles", json={"url": args.url or args.file})
        res.raise_for_status()
        print(json.dumps(res.json(), indent=2))
    return 0


def cmd_plugins(_args: argparse.Namespace) -> int:
    with _client(_args.base, _args.key) as client:
        res = client.get("/v1/plugins")
        res.raise_for_status()
        print(json.dumps(res.json(), indent=2))
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    with _client(args.base, args.key) as client:
        health = client.get("/health")
        system = client.get("/v1/system")
        print(json.dumps({"health": health.json(), "system": system.json()}, indent=2))
        return 0 if health.is_success and system.is_success else 1


def cmd_worker(_args: argparse.Namespace) -> int:
    from apps.worker.main import run

    run()
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="mediacore", description="MediaCore CLI")
    parser.add_argument("--base", default=DEFAULT_BASE)
    parser.add_argument("--key", default=DEFAULT_KEY)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("analyze")
    p.add_argument("url")
    p.set_defaults(func=cmd_analyze)

    p = sub.add_parser("download")
    p.add_argument("url")
    p.add_argument("--format", default="original")
    p.set_defaults(func=cmd_download)

    p = sub.add_parser("convert")
    p.add_argument("file")
    p.add_argument("--container", default="mp4")
    p.set_defaults(func=cmd_convert)

    p = sub.add_parser("subtitle")
    p.add_argument("file", nargs="?")
    p.add_argument("--url")
    p.set_defaults(func=cmd_subtitle)

    p = sub.add_parser("plugin")
    plugin_sub = p.add_subparsers(dest="plugin_cmd", required=True)
    pl = plugin_sub.add_parser("install")
    pl.set_defaults(func=lambda a: print("Plugin install registry coming in v0.5") or 0)
    pl = plugin_sub.add_parser("list")
    pl.set_defaults(func=cmd_plugins)

    p = sub.add_parser("worker")
    worker_sub = p.add_subparsers(dest="worker_cmd", required=True)
    w = worker_sub.add_parser("start")
    w.set_defaults(func=cmd_worker)

    p = sub.add_parser("doctor")
    p.set_defaults(func=cmd_doctor)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except httpx.HTTPError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
