import json
from pathlib import Path

def load_config(config_path):
	config_path = Path(config_path)

	if not config_path.exists():
		raise FileNotFoundError(f"Config file not found: {config_path}")

	with open(config_path, "r", encoding="utf-8") as file:
		config = json.load(file)

	return config