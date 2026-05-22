from pydantic import BaseModel


class PredictionRequest(BaseModel):
    age: int
    sleep_duration: float
    quality_of_sleep: int
    physical_activity_level: int
    stress_level: int
    heart_rate: int
    daily_steps: int


class PredictionResponse(BaseModel):
    predicted_systolic_bp: float
    model_name: str


class SchemaDriftRequest(BaseModel):
    reference_columns: list[str]
    current_columns: list[str]