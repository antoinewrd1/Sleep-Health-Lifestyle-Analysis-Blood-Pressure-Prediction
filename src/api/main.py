from fastapi import FastAPI
from pydantic import BaseModel

from src.database.db import log_prediction


app = FastAPI(
    title="Sleep Health Blood Pressure Prediction API",
    version="1.0.0",
)


class PredictionInput(BaseModel):
    age: int
    sleep_duration: float
    quality_of_sleep: int
    physical_activity_level: int
    stress_level: int
    heart_rate: int
    daily_steps: int


def simple_prediction_rule(payload):
    prediction = (
        95
        + 0.25 * payload.age
        - 0.7 * payload.sleep_duration
        + 0.45 * payload.stress_level
        + 0.08 * payload.heart_rate
        - 0.0002 * payload.daily_steps
    )

    return round(prediction, 2)


@app.get("/")
def root():
    return {
        "message": "Sleep Health Blood Pressure Prediction API is running"
    }


@app.post("/predict")
def predict(payload: PredictionInput):
    prediction = simple_prediction_rule(payload)

    log_prediction(
        model_name="simple_rule_baseline",
        input_payload=payload.model_dump(),
        prediction=prediction,
    )

    return {
        "predicted_systolic_bp": prediction,
        "model_name": "simple_rule_baseline",
    }