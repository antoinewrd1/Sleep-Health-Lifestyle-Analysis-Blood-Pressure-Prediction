import pandas as pd

from src.results_manager import (
    save_experiment_results,
    load_experiment_results,
)


def test_save_and_load_experiment_results(tmp_path):
    df = pd.DataFrame(
        {
            "Model": ["Random Forest"],
            "RMSE": [5.1],
        }
    )

    output_path = tmp_path / "results.csv"

    save_experiment_results(df, output_path)

    loaded = load_experiment_results(output_path)

    assert loaded.loc[0, "Model"] == "Random Forest"
    assert loaded.loc[0, "RMSE"] == 5.1