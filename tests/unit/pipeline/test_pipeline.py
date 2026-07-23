import pytest

from packages.core.pipeline import Pipeline, PipelineStage

pytestmark = pytest.mark.unit


def test_pipeline_stages():
    p = Pipeline("https://cdn.example.com/a.mp4")
    p.set_metadata({"title": "a", "formats": [{"id": "original"}]})
    assert p.ctx.stage == PipelineStage.METADATA
    p.set_downloaded("/tmp/a.mp4")
    assert p.ctx.stage == PipelineStage.DOWNLOAD
