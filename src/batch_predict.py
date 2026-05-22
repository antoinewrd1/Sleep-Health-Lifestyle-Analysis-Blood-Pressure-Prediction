from pathlib import Path

import joblib
import pandas as pd


def run_batch_predictions(
    model_path,
    input_csv_path,
    output_csv_path,
):
    model_path = Path(model_path)
    input_csv_path = Path(input_csv_path)
    output_csv_path = Path(output_csv_path)

    if not model_path.exists():
        raise FileNotFoundError(f"Model not found: {model_path}")

    if not input_csv_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {input_csv_path}")

    model = joblib.load(model_path)

    input_df = pd.read_csv(input_csv_path)

    predictions = model.predict(input_df)

    output_df = input_df.copy()
    output_df["predicted_systolic_bp"] = predictions

    output_csv_path.parent.mkdir(parents=True, exist_ok=True)
    output_df.to_csv(output_csv_path, index=False)

    return output_df
