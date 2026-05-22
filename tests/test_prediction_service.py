from src.api.schemas import PredictionRequest
from src.services.prediction_service import PredictionService


def test_prediction_service_returns_float_prediction():
    service = PredictionService()

    request = PredictionRequest(
        age=40,
        sleep_duration=7.0,
        quality_of_sleep=7,
        physical_activity_level=50,
        stress_level=5,
        heart_rate=75,
        daily_steps=7000,
    )

    prediction = service.predict_systolic_bp(request)

    assert isinstance(prediction, float)
    assert prediction > 0