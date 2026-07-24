from pathlib import Path
from unittest.mock import patch

import pytest

from packages.core.postprocess import PostprocessStep, extract_audio_track, remux

pytestmark = pytest.mark.unit


def test_remux_delegates(tmp_path: Path):
    src = tmp_path / "in.mkv"
    dest = tmp_path / "out.mp4"
    src.write_bytes(b"x")
    with patch("packages.core.postprocess.convert_media", return_value=dest) as convert:
        assert remux(src, dest) == dest
        convert.assert_called_once_with(src, dest)


def test_extract_audio_delegates(tmp_path: Path):
    src = tmp_path / "in.mp4"
    dest = tmp_path / "out.mp3"
    src.write_bytes(b"x")
    with patch("packages.core.postprocess.extract_audio", return_value=dest) as extract:
        assert extract_audio_track(src, dest) == dest
        extract.assert_called_once()
    assert PostprocessStep.EXTRACT_AUDIO.value == "extract_audio"
