import pytest

from packages.core.parser import hostname, is_direct_media_url, path_segments
from packages.core.validator import validate_url
from packages.testkit.generators import make_metadata

pytestmark = pytest.mark.benchmark


def test_bench_validate_url(benchmark):
    benchmark(validate_url, "https://cdn.example.com/clip.mp4")


def test_bench_hostname(benchmark):
    benchmark(hostname, "https://cdn.example.com/a/b/c.mp4")


def test_bench_is_direct_media(benchmark):
    benchmark(is_direct_media_url, "https://cdn.example.com/a.mp4")


def test_bench_path_segments(benchmark):
    benchmark(path_segments, "https://cdn.example.com/a/b/c.mp4")


def test_bench_metadata_to_dict(benchmark):
    meta = make_metadata()
    benchmark(meta.to_dict)
