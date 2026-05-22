from pathlib import Path


class ReportService:
    def __init__(self, reports_dir="reports"):
        self.reports_dir = Path(reports_dir)
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def create_prediction_report(self, predictions, output_name="prediction_report.md"):
        output_path = self.reports_dir / output_name

        lines = [
            "# Prediction Report",
            "",
            f"Total Predictions: {len(predictions)}",
            "",
            "## Recent Predictions",
            "",
        ]

        for item in predictions:
            lines.append(
                f"- Model: {item['model_name']} | Prediction: {item['prediction']}"
            )

        output_path.write_text("\n".join(lines), encoding="utf-8")

        return output_path

    def get_latest_report_path(self):
        reports = sorted(self.reports_dir.glob("*.md"))

        if not reports:
            return None

        return reports[-1]