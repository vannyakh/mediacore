from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_no_critical_empty_dirs():
    critical = [
        ROOT / "packages" / "auth",
        ROOT / "packages" / "cache",
        ROOT / "packages" / "config",
        ROOT / "packages" / "logging",
        ROOT / "packages" / "scheduler",
        ROOT / "packages" / "telemetry",
        ROOT / "packages" / "sdk_generator",
        ROOT / "plugins" / "whisper",
        ROOT / "plugins" / "discord",
        ROOT / "helm" / "mediacore",
        ROOT / "scripts",
        ROOT / "benchmarks",
        ROOT / "sdk" / "csharp",
        ROOT / "apps" / "desktop" / "src",
        ROOT / "apps" / "studio" / "src",
    ]
    for path in critical:
        assert path.exists(), f"missing {path}"
        files = list(path.rglob("*"))
        assert any(p.is_file() for p in files), f"empty scaffold: {path}"


def test_all_plugins_have_manifest():
    plugins_root = ROOT / "plugins"
    for entry in plugins_root.iterdir():
        if entry.is_dir():
            assert (entry / "plugin.py").exists(), f"missing plugin.py in {entry.name}"


def test_plugin_loader_discovers_all():
    from packages.plugins.loader import PluginLoader

    loader = PluginLoader(root=ROOT / "plugins")
    plugins = loader.discover()
    assert len(plugins) >= 14


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
