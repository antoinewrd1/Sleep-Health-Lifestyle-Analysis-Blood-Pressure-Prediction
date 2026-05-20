import json

from src.experiment_tracker import save_experiment_metadata


def test_save_experiment_metadata_creates_json_file(tmp_path):
    output_path = tmp_path / "experiment.json"

    metadata = {
        "best_model": "Random Forest",
        "metric": "RMSE",
    }

    saved_path = save_experiment_metadata(metadata, output_path)

    assert saved_path.exists()

    loaded = json.loads(saved_path.read_text(encoding="utf-8"))

    assert loaded["best_model"] == "Random Forest"
    assert loaded["metric"] == "RMSE"
    assert "created_at_utc" in loaded