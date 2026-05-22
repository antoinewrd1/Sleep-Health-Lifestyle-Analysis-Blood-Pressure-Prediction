from pathlib import Path


def check_required_paths(paths):
    missing = []

    for path in paths:
        if not Path(path).exists():
            missing.append(str(path))

    if missing:
        raise FileNotFoundError(f"Missing required paths: {missing}")

    return True