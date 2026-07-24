from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_download_tool_core_dirs():
    critical = [
        ROOT / "apps" / "api",
        ROOT / "apps" / "cli",
        ROOT / "apps" / "worker",
        ROOT / "packages" / "core",
        ROOT / "packages" / "engine",
        ROOT / "packages" / "registry",
        ROOT / "packages" / "queue",
        ROOT / "packages" / "storage",
        ROOT / "packages" / "config",
        ROOT / "packages" / "logging",
        ROOT / "plugins" / "ffmpeg",
        ROOT / "plugins" / "storage-local",
        ROOT / "providers" / "modules",
        ROOT / "scripts",
    ]
    for path in critical:
        assert path.exists(), f"missing {path}"
        files = list(path.rglob("*"))
        assert any(p.is_file() for p in files), f"empty scaffold: {path}"


def test_removed_product_surfaces_gone():
    for name in (
        "benchmarks",
        "crates",
        "helm",
        "patches",
        "apps/dashboard",
        "apps/desktop",
        "apps/studio",
        "apps/gateway",
        "apps/scheduler",
        "packages/telemetry",
        "packages/scheduler",
        "packages/sdk_generator",
        "packages/mediacore_benchmark",
        "plugins/whisper",
        "plugins/telegram",
        "plugins/discord",
        "packages/storage/azure.py",
        "packages/storage/s3_compatible.py",
        "packages/storage/ftp.py",
        "extractor",
    ):
        assert not (ROOT / name).exists(), f"should be removed: {name}"


def test_sdk_packages_present():
    for rel in (
        "sdk/python/mediacore_sdk/__init__.py",
        "sdk/javascript/package.json",
        "sdk/typescript/package.json",
        "sdk/php/composer.json",
        "sdk/go/go.mod",
    ):
        assert (ROOT / rel).is_file(), f"missing SDK package: {rel}"


def test_all_plugins_have_manifest():
    plugins_root = ROOT / "plugins"
    for entry in plugins_root.iterdir():
        if entry.is_dir() and not entry.name.startswith(".") and entry.name != "__pycache__":
            assert (entry / "plugin.py").exists(), f"missing plugin.py in {entry.name}"


def test_plugin_loader_discovers_download_plugins():
    from packages.plugins.loader import PluginLoader

    loader = PluginLoader(root=ROOT / "plugins")
    plugins = loader.discover()
    names = {p.name for p in plugins}
    assert "mediacore-plugin-ffmpeg" in names
    assert "mediacore-plugin-storage-local" in names
    assert len(plugins) == 2


def test_legacy_shims_removed():
    for name in ("extractor", "ffmpeg", "storage", "jobqueue", "queue"):
        path = ROOT / name
        assert not path.exists(), f"legacy path should be gone: {path}"
    assert not (ROOT / "providers" / "stubs").exists()
    assert (ROOT / "providers" / "modules").is_dir()


def test_working_provider_packages_have_provider_py():
    """No empty providers/<name>/ shells (catalog lives under modules/)."""
    skip = {"modules", "data", "platforms", "__pycache__"}
    for entry in (ROOT / "providers").iterdir():
        if not entry.is_dir() or entry.name in skip:
            continue
        if entry.name.startswith("."):
            continue
        assert (entry / "provider.py").is_file(), (
            f"working provider package missing provider.py: {entry.name} "
            "(use providers/modules/ for catalog-only, or delete empty shells)"
        )
