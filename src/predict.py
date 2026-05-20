from pathlib import Path
import joblib
import pandas as pd


def load_model(model_path):
    model_path = Path(model_path)

    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")

    return joblib.load(model_path)


def predict_from_csv(model_path, input_csv_path, output_csv_path):
    model = load_model(model_path)

    input_csv_path = Path(input_csv_path)
    output_csv_path = Path(output_csv_path)

    if not input_csv_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_csv_path}")

    df = pd.read_csv(input_csv_path)

    predictions = model.predict(df)

    output_csv_path.parent.mkdir(parents=True, exist_ok=True)

    results = df.copy()
    results["prediction"] = predictions
    results.to_csv(output_csv_path, index=False)

    return results