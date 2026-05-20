import pandas as pd

from src.reporting import write_markdown_report


def test_write_markdown_report_creates_file(tmp_path):
    results = pd.DataFrame(
        {
            "Model": ["Baseline", "Random Forest"],
            "Test RMSE": [10.0, 5.0],
            "Test R2": [0.0, 0.75],
        }
    )

    output_path = tmp_path / "model_report.md"

    write_markdown_report(results, output_path)

    assert output_path.exists()

    content = output_path.read_text(encoding="utf-8")

    assert "Random Forest" in content
    assert "Model Evaluation Report" in content