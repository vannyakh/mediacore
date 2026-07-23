"""MediaCore CLI entrypoint."""

from __future__ import annotations

import argparse
import sys

import httpx

from apps.cli import commands
from apps.cli.client import DEFAULT_BASE, DEFAULT_KEY, eprint, format_http_error, resolve_base, resolve_key


def _add_wait_flags(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--wait",
        action="store_true",
        help="Poll job status until terminal state",
    )
    parser.add_argument(
        "--wait-timeout",
        type=float,
        default=120.0,
        help="Seconds to wait when --wait is set (default: 120)",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="mediacore", description="MediaCore CLI")
    parser.add_argument(
        "--base",
        default=None,
        help=f"API base URL (env MEDIACORE_BASE, default {DEFAULT_BASE})",
    )
    parser.add_argument(
        "--key",
        default=None,
        help=f"API key (env MEDIACORE_API_KEY, default {DEFAULT_KEY})",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("analyze", help="Analyze a media URL")
    p.add_argument("url")
    p.set_defaults(func=commands.cmd_analyze)

    p = sub.add_parser("download", help="Enqueue a download job")
    p.add_argument("url")
    p.add_argument("--format", default="original")
    _add_wait_flags(p)
    p.set_defaults(func=commands.cmd_download)

    p = sub.add_parser("convert", help="Enqueue a convert job for a local file")
    p.add_argument("file")
    p.add_argument("--container", default="mp4")
    _add_wait_flags(p)
    p.set_defaults(func=commands.cmd_convert)

    p = sub.add_parser("subtitle", help="Enqueue a subtitles job")
    p.add_argument("file", nargs="?")
    p.add_argument("--url")
    _add_wait_flags(p)
    p.set_defaults(func=commands.cmd_subtitle)

    p = sub.add_parser("plugin", help="Manage plugins")
    plugin_sub = p.add_subparsers(dest="plugin_cmd", required=True)
    pl = plugin_sub.add_parser("install", help="Install a plugin from a local path or plugins/ name")
    pl.add_argument("target", help="Directory path or plugin name under plugins/")
    pl.add_argument(
        "--plugins-root",
        default=None,
        help="Override plugins directory (tests / custom layouts)",
    )
    pl.set_defaults(func=commands.cmd_plugin_install)
    pl = plugin_sub.add_parser("list", help="List discovered plugins")
    pl.set_defaults(func=commands.cmd_plugin_list)

    p = sub.add_parser("worker", help="Worker process controls")
    worker_sub = p.add_subparsers(dest="worker_cmd", required=True)
    w = worker_sub.add_parser("start", help="Start the Dramatiq worker")
    w.set_defaults(func=commands.cmd_worker)

    p = sub.add_parser("doctor", help="Check API, plugins, and ffmpeg")
    p.set_defaults(func=commands.cmd_doctor)

    p = sub.add_parser("events", help="List or follow MediaCore lifecycle events")
    p.add_argument("--job-id", default=None, help="Filter by job id")
    p.add_argument("--follow", "-f", action="store_true", help="Follow SSE stream")
    p.add_argument("--limit", type=int, default=50, help="History limit when not following")
    p.set_defaults(func=commands.cmd_events)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.base = resolve_base(args.base)
    args.key = resolve_key(args.key)
    try:
        return int(args.func(args))
    except httpx.HTTPError as exc:
        eprint(f"error: {format_http_error(exc)}")
        return 1
    except TimeoutError as exc:
        eprint(f"error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
