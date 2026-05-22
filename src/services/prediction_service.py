from src.api.schemas import PredictionRequest


class PredictionService:
    def __init__(self, model_name="rule_based_baseline"):
        self.model_name = model_name

    def predict_systolic_bp(self, request: PredictionRequest) -> float:
        prediction = (
            95
            + 0.25 * request.age
            - 0.70 * request.sleep_duration
            + 0.30 * request.quality_of_sleep
            + 0.03 * request.physical_activity_level
            + 0.45 * request.stress_level
            + 0.08 * request.heart_rate
            - 0.0002 * request.daily_steps
        )

        return round(float(prediction), 2)

    def predict_from_dict(self, payload: dict) -> dict:
        request = PredictionRequest(**payload)
        prediction = self.predict_systolic_bp(request)

        return {
            "predicted_systolic_bp": prediction,
            "model_name": self.model_name,
        }