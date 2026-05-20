import json

from src.config_loader import load_config

def test_load_config_reads_json_file(tmp_path):
	config_path = tmp_path / "config.json"

	expected = {
		"target_column": "Systolic",
		"random_state": 42
	}

	config_path.write_text(json.dumps(expected), encoding="utf-8")

	actual = load_config(config_path)

	assert actual == expected