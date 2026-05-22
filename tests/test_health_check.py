import pytest

from src.health_check import check_required_paths


def test_check_required_paths_passes_for_existing_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("test", encoding="utf-8")

    assert check_required_paths([file_path]) is True


def test_check_required_paths_raises_for_missing_file(tmp_path):
    missing_file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        check_required_paths([missing_file])