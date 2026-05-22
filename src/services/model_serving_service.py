from pathlib import Path
import joblib
import pandas as pd


class ModelServingService:
    def __init__(self, model_path="models/best_model.joblib"):
        self.model_path = Path(model_path)
        self.model = None

    def load(self):
        if not self.model_path.exists():
            raise FileNotFoundError(f"Model artifact not found: {self.model_path}")

        self.model = joblib.load(self.model_path)

        return self.model

    def predict_dataframe(self, df: pd.DataFrame):
        if self.model is None:
            self.load()

        return self.model.predict(df)

    def predict_single(self, payload: dict):
        df = pd.DataFrame([payload])

        prediction = self.predict_dataframe(df)[0]

        return float(prediction)