import pytest

from packages.core.pipeline import Pipeline
from packages.testkit.generators import make_huge_metadata

pytestmark = pytest.mark.stress


def test_huge_metadata_pipeline():
    meta = make_huge_metadata(2000)
    assert len(meta.formats) == 2000
    p = Pipeline("https://cdn.example.com/huge.mp4")
    p.set_metadata(meta.to_dict())
    assert len(p.ctx.formats) == 2000
    snap = p.snapshot()
    assert snap["metadata"]["title"] == "huge"


def test_many_pipeline_jobs():
    pipelines = [Pipeline(f"https://cdn.example.com/{i}.mp4") for i in range(500)]
    for i, p in enumerate(pipelines):
        p.set_metadata({"title": str(i), "formats": [{"id": "original"}]})
        p.set_downloaded(f"/tmp/{i}.mp4")
    assert all(p.ctx.artifact_path for p in pipelines)
