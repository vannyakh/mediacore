import pytest

from packages.mediacore_benchmark.compare import compare_summaries, detect_regressions

pytestmark = pytest.mark.unit


def test_detect_regression():
    baseline = {
        "benchmarks": [{"name": "python/analyze", "mean_s": 0.001}],
    }
    current = {
        "benchmarks": [{"name": "python/analyze", "mean_s": 0.002}],
    }
    rows = compare_summaries(baseline, current)
    bad = detect_regressions(rows, threshold=0.15)
    assert len(bad) == 1
    assert bad[0]["name"] == "python/analyze"


def test_no_regression_within_threshold():
    baseline = {"benchmarks": [{"name": "x", "mean_s": 1.0}]}
    current = {"benchmarks": [{"name": "x", "mean_s": 1.10}]}
    rows = compare_summaries(baseline, current)
    assert detect_regressions(rows, threshold=0.15) == []
