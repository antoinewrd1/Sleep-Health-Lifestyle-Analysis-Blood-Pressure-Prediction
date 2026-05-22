from src.admin.admin_service import AdminService


class FakeRepository:
    def get_recent_predictions(self, limit=50):
        return [
            {"prediction": 120.0},
            {"prediction": 130.0},
        ]


class FakeReportService:
    def create_prediction_report(self, predictions, output_name):
        return "reports/admin_prediction_report.md"


def test_admin_service_returns_prediction_summary():
    service = AdminService(
        repository=FakeRepository(),
        report_service=FakeReportService(),
    )

    summary = service.get_prediction_summary()

    assert summary["total_predictions"] == 2
    assert summary["average_prediction"] == 125.0


def test_admin_service_generates_report():
    service = AdminService(
        repository=FakeRepository(),
        report_service=FakeReportService(),
    )

    report_path = service.generate_admin_report()

    assert report_path == "reports/admin_prediction_report.md"