import pandas as pd


def compare_dataset_schema(reference_df, current_df):
    reference_columns = set(reference_df.columns)
    current_columns = set(current_df.columns)

    return {
        "missing_columns": sorted(reference_columns - current_columns),
        "new_columns": sorted(current_columns - reference_columns),
    }


def compare_numeric_means(reference_df, current_df, numeric_columns, threshold=0.10):
    drift_results = {}

    for column in numeric_columns:
        if column not in reference_df.columns or column not in current_df.columns:
            continue

        reference_mean = reference_df[column].mean()
        current_mean = current_df[column].mean()

        if reference_mean == 0:
            continue

        percent_change = abs(current_mean - reference_mean) / abs(reference_mean)

        drift_results[column] = {
            "reference_mean": reference_mean,
            "current_mean": current_mean,
            "percent_change": percent_change,
            "drift_detected": bool(percent_change > threshold),
        }

    return drift_results


def summarize_prediction_distribution(predictions):
    prediction_series = pd.Series(predictions)

    return {
        "count": int(prediction_series.count()),
        "mean": float(prediction_series.mean()),
        "min": float(prediction_series.min()),
        "max": float(prediction_series.max()),
        "std": float(prediction_series.std()),
    }