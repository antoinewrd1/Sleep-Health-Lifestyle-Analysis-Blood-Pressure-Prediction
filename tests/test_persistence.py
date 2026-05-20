import pandas as pd

from src.persistence import save_dataframe


def test_save_dataframe_creates_csv_file(tmp_path):
    df = pd.DataFrame(
        {
            "Model": ["Random Forest"],
            "Test RMSE": [5.25],
        }
    )

    output_path = tmp_path / "results.csv"

    saved_path = save_dataframe(df, output_path)

    assert saved_path.exists()

    loaded = pd.read_csv(saved_path)

    assert loaded.loc[0, "Model"] == "Random Forest"
    assert loaded.loc[0, "Test RMSE"] == 5.25