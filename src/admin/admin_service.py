from src.repositories.prediction_repository import PredictionRepository
from src.services.report_service import ReportService


class AdminService:
    def __init__(self, repository=None, report_service=None):
        self.repository = repository or PredictionRepository()
        self.report_service = report_service or ReportService()

    def get_prediction_summary(self, limit=50):
        predictions = self.repository.get_recent_predictions(limit=limit)

        if not predictions:
            return {
                "total_predictions": 0,
                "average_prediction": None,
            }

        values = [item["prediction"] for item in predictions]

        return {
            "total_predictions": len(values),
            "average_prediction": sum(values) / len(values),
            "min_prediction": min(values),
            "max_prediction": max(values),
        }

    def generate_admin_report(self):
        predictions = self.repository.get_recent_predictions(limit=100)

        return self.report_service.create_prediction_report(
            predictions,
            output_name="admin_prediction_report.md",
        )