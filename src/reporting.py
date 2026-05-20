from pathlib import Path


def write_markdown_report(test_results_df, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    best_model = test_results_df.sort_values("Test RMSE").iloc[0]

    report = f"""# Model Evaluation Report

## Best Model

Model: {best_model["Model"]}

Test RMSE: {best_model["Test RMSE"]:.4f}

Test R2: {best_model["Test R2"]:.4f}

## Full Results

{test_results_df.to_markdown(index=False)}
"""

    output_path.write_text(report, encoding="utf-8")

    return output_path