"""MediaCore CLI entrypoint."""

from __future__ import annotations

import argparse
import sys

import httpx

from apps.cli import commands
from apps.cli.client import (
    DEFAULT_BASE,
    DEFAULT_KEY,
    eprint,
    format_http_error,
    resolve_base,
    resolve_key,
    set_verbosity,
)

# Subcommands stay available; bare URL / -a batch uses yt-dlp-like "get" mode.
_SUBCOMMANDS = frozenset(
    {
        "analyze",
        "download",
        "process",
        "convert",
        "subtitle",
        "plugin",
        "worker",
        "doctor",
        "events",
        "providers",
        "get",
        "help",
    }
)

# Flags that take a following value (for argv rewrite)
_VALUE_FLAGS = frozenset(
    {
        "--base",
        "--key",
        "-o",
        "--output",
        "-a",
        "--batch-file",
        "-f",
        "--format",
        "--wait-timeout",
        "--container",
    }
)


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


def _add_common_media_flags(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-F",
        "--list-formats",
        action="store_true",
        help="List formats from analyze (like yt-dlp -F); no download",
    )
    parser.add_argument(
        "-s",
        "--simulate",
        action="store_true",
        help="Analyze only; do not enqueue download",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Local output path or simple template with {title}/{id} (after permitted download)",
    )
    parser.add_argument(
        "-f",
        "--format",
        default="original",
        help="Format id (default: original)",
    )
    parser.add_argument(
        "-a",
        "--batch-file",
        default=None,
        help="File with one URL per line (# comments allowed)",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Quiet: less stdout",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose: print request hints to stderr",
    )


def rewrite_argv_for_url_mode(argv: list[str]) -> list[str]:
    """If first positional is not a subcommand, insert ``get`` (URL-first UX)."""
    if not argv:
        return argv
    # Keep parent-only options before the subcommand so argparse still binds them.
    parent_value = {"--base", "--key"}
    i = 0
    prefix: list[str] = []
    while i < len(argv):
        if argv[i] in parent_value and i + 1 < len(argv):
            prefix.extend(argv[i : i + 2])
            i += 2
            continue
        break
    rest = argv[i:]
    j = 0
    while j < len(rest):
        arg = rest[j]
        if arg in _VALUE_FLAGS and j + 1 < len(rest):
            j += 2
            continue
        if arg.startswith("-"):
            j += 1
            continue
        break
    if j >= len(rest):
        return argv
    if rest[j] in _SUBCOMMANDS:
        return argv
    return [*prefix, "get", *rest]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mediacore",
        description=(
            "MediaCore CLI — permitted analyze/download/process for direct media, "
            "share links, and public APIs. YouTube-class sites are metadata (-s) "
            "unless a permitted download path exists. URL-first: mediacore [opts] URL."
        ),
    )
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

    p = sub.add_parser(
        "get",
        help="URL-first: analyze / list formats / download (permitted sources only)",
    )
    p.add_argument("urls", nargs="*", help="One or more media URLs")
    _add_common_media_flags(p)
    _add_wait_flags(p)
    p.set_defaults(func=commands.cmd_get, wait=True)

    p = sub.add_parser("analyze", help="Analyze a media URL")
    p.add_argument("url")
    _add_common_media_flags(p)
    p.set_defaults(func=commands.cmd_analyze)

    p = sub.add_parser("download", help="Enqueue a download job")
    p.add_argument("url", nargs="?")
    _add_common_media_flags(p)
    _add_wait_flags(p)
    p.set_defaults(func=commands.cmd_download)

    p = sub.add_parser(
        "process",
        help="Download then convert (permitted sources + ffmpeg plugin)",
    )
    p.add_argument("url")
    p.add_argument("--format", default="original")
    p.add_argument("--container", default="mp4")
    p.add_argument(
        "--wait-timeout",
        type=float,
        default=180.0,
        help="Seconds to wait per job step (default: 180)",
    )
    p.add_argument("-q", "--quiet", action="store_true")
    p.add_argument("-v", "--verbose", action="store_true")
    p.set_defaults(func=commands.cmd_process)

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
    pl = plugin_sub.add_parser(
        "install", help="Install a plugin from a local path or plugins/ name"
    )
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

    p = sub.add_parser(
        "providers",
        help="List working providers or search the platform catalog",
    )
    prov_sub = p.add_subparsers(dest="providers_cmd")
    pl = prov_sub.add_parser("list", help="List working providers (and catalog summary)")
    pl.add_argument(
        "--status",
        default=None,
        help="Filter by status (active, metadata_only, not_configured, …)",
    )
    pl.add_argument(
        "--download-only",
        action="store_true",
        help="Show only download-capable providers (active/available)",
    )
    pl.set_defaults(func=commands.cmd_providers_list)
    ps = prov_sub.add_parser("search", help="Search catalog extractors by name")
    ps.add_argument("query", help="Search query")
    ps.add_argument("--limit", type=int, default=50, help="Max results (default: 50)")
    ps.set_defaults(func=commands.cmd_providers_search)
    p.set_defaults(func=commands.cmd_providers_list, status=None, download_only=False)
    return parser


def main(argv: list[str] | None = None) -> int:
    raw = list(sys.argv[1:] if argv is None else argv)
    raw = rewrite_argv_for_url_mode(raw)
    parser = build_parser()
    args = parser.parse_args(raw)
    args.base = resolve_base(args.base)
    args.key = resolve_key(args.key)
    set_verbosity(quiet=bool(getattr(args, "quiet", False)), verbose=bool(getattr(args, "verbose", False)))
    try:
        return int(args.func(args))
    except httpx.HTTPError as exc:
        eprint(f"error: {format_http_error(exc)}")
        return 1
    except TimeoutError as exc:
        eprint(f"error: {exc}")
        return 1
    except FileNotFoundError as exc:
        eprint(f"error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
