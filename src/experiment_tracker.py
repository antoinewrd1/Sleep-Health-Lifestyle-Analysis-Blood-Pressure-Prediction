import json
from datetime import datetime, timezone
from pathlib import Path


def save_experiment_metadata(metadata, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    metadata = {
        **metadata,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
    }

    output_path.write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    return output_path