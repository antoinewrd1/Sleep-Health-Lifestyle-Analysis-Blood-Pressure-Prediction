import pandas as pd

from src.monitoring import (
    compare_dataset_schema,
    compare_numeric_means,
    summarize_prediction_distribution,
)


def test_compare_dataset_schema_detects_missing_and_new_columns():
    reference_df = pd.DataFrame(
        {
            "Age": [30],
            "Stress Level": [5],
        }
    )

    current_df = pd.DataFrame(
        {
            "Age": [30],
            "Heart Rate": [70],
        }
    )

    result = compare_dataset_schema(reference_df, current_df)

    assert result["missing_columns"] == ["Stress Level"]
    assert result["new_columns"] == ["Heart Rate"]


def test_compare_numeric_means_detects_drift():
    reference_df = pd.DataFrame({"Age": [30, 40, 50]})
    current_df = pd.DataFrame({"Age": [60, 70, 80]})

    result = compare_numeric_means(
        reference_df,
        current_df,
        numeric_columns=["Age"],
        threshold=0.10,
    )

    assert result["Age"]["drift_detected"] is True


def test_summarize_prediction_distribution_returns_summary():
    predictions = [110, 120, 130]

    summary = summarize_prediction_distribution(predictions)

    assert summary["count"] == 3
    assert summary["mean"] == 120
    assert summary["min"] == 110
    assert summary["max"] == 130