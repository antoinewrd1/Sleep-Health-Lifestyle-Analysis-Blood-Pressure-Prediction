from pathlib import Path
import pandas as pd


def save_experiment_results(results_df, output_path):
    output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    results_df.to_csv(output_path, index=False)

    return output_path


def load_experiment_results(results_path):
    results_path = Path(results_path)

    if not results_path.exists():
        raise FileNotFoundError(
            f"Results file not found: {results_path}"
        )

    return pd.read_csv(results_path)