from pathlib import Path

def write_markdown_report(metrics_df, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    best_model = metrics_df.sort_values("Test RMSE").iloc[0]

    report = f"""# Model Evaluation Report

    ## Best Model

    **Model:** {best_model["Model"]}

    **Test RMSE:** {best_model["Test RMSE"]:.4f}

    **Test R2:** {best_model["Test R2"]:.4f}

    ## Full Results

    {metrics_df.to_markdown(index=False)}
    """

        output_path.write_text(report, encoding="utf-8")

    