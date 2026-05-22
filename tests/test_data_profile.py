import pandas as pd

from src.data_profile import generate_data_profile


def test_generate_data_profile_returns_expected_summary(tmp_path):
    df = pd.DataFrame(
        {
            "Age": [30, 40, None],
            "Stress Level": [3, 5, 7],
        }
    )

    output_path = tmp_path / "profile.txt"

    profile = generate_data_profile(df, output_path)

    assert profile["row_count"] == 3
    assert profile["column_count"] == 2
    assert profile["missing_values"]["Age"] == 1
    assert output_path.exists()