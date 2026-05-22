from pathlib import Path
import pandas as pd

from src.services.model_serving_service import ModelServingService


class BatchPredictionJob:
    def __init__(self, model_path="models/best_model.joblib"):
        self.model_service = ModelServingService(model_path=model_path)

    def run(self, input_csv_path, output_csv_path):
        input_csv_path = Path(input_csv_path)
        output_csv_path = Path(output_csv_path)

        if not input_csv_path.exists():
            raise FileNotFoundError(f"Input CSV not found: {input_csv_path}")

        df = pd.read_csv(input_csv_path)

        predictions = self.model_service.predict_dataframe(df)

        output_df = df.copy()
        output_df["predicted_systolic_bp"] = predictions

        output_csv_path.parent.mkdir(parents=True, exist_ok=True)
        output_df.to_csv(output_csv_path, index=False)

        return output_df