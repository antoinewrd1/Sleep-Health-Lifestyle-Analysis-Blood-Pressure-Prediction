from fastapi import Depends, UploadFile, File
import pandas as pd
import tempfile

from src.auth.security import verify_api_key
from src.admin.admin_service import AdminService
from src.jobs.batch_prediction_job import BatchPredictionJob
from fastapi import APIRouter

from src.api.schemas import (
    PredictionRequest,
    PredictionResponse,
    SchemaDriftRequest,
)
from src.services.prediction_service import PredictionService
from src.services.monitoring_service import MonitoringService
from src.services.report_service import ReportService
from src.repositories.prediction_repository import PredictionRepository


router = APIRouter()

prediction_service = PredictionService()
monitoring_service = MonitoringService()
repository = PredictionRepository()
report_service = ReportService()

@router.get("/")
def root():
    return {
        "message": "Sleep Health Blood Pressure Prediction API is running"
    }

@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "sleep-health-bp-platform",
    }


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    prediction = prediction_service.predict_systolic_bp(request)

    repository.save_prediction(
        model_name=prediction_service.model_name,
        payload=request.model_dump(),
        prediction=prediction,
    )

    return {
        "predicted_systolic_bp": prediction,
        "model_name": prediction_service.model_name,
    }


@router.get("/predictions/recent")
def recent_predictions(limit: int = 10):
    return {
        "predictions": repository.get_recent_predictions(limit=limit)
    }


@router.post("/monitoring/schema-drift")
def schema_drift(request: SchemaDriftRequest):
    result = monitoring_service.compare_schema(
        reference_columns=request.reference_columns,
        current_columns=request.current_columns,
    )

    return result


@router.post("/reports/predictions")
def create_prediction_report():
    predictions = repository.get_recent_predictions(limit=25)
    report_path = report_service.create_prediction_report(predictions)

    return {
        "report_path": str(report_path),
        "prediction_count": len(predictions),
    }


@router.get("/reports/latest")
def latest_report():
    report_path = report_service.get_latest_report_path()

    if report_path is None:
        return {
            "message": "No reports available"
        }

    return {
        "report_path": str(report_path)
    }

@router.get("/admin/summary", dependencies=[Depends(verify_api_key)])
def admin_summary():
    service = AdminService()

    return service.get_prediction_summary()


@router.post("/admin/report", dependencies=[Depends(verify_api_key)])
def admin_report():
    service = AdminService()

    report_path = service.generate_admin_report()

    return {
        "report_path": str(report_path)
    }


@router.post("/batch-predict", dependencies=[Depends(verify_api_key)])
def batch_predict(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_input:
        temp_input.write(file.file.read())
        temp_input_path = temp_input.name

    output_path = "outputs/api_batch_predictions.csv"

    job = BatchPredictionJob()
    result_df = job.run(temp_input_path, output_path)

    return {
        "rows_scored": len(result_df),
        "output_path": output_path,
    }