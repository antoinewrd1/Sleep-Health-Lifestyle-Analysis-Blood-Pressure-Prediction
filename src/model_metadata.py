from datetime import datetime, timezone


def build_model_metadata(
    model_name,
    metrics,
    training_rows,
):
    return {
        "model_name": model_name,
        "metrics": metrics,
        "training_rows": training_rows,
        "created_at_utc": datetime.now(
            timezone.utc
        ).isoformat(),
    }