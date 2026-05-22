from dataclasses import dataclass
from datetime import datetime


@dataclass
class PredictionLog:
    id: int | None
    created_at_utc: datetime
    model_name: str
    input_payload: str
    prediction: float
    user_id: str | None = None


@dataclass
class ModelRun:
    id: int | None
    created_at_utc: datetime
    model_name: str
    rmse: float
    r2: float
    artifact_path: str
