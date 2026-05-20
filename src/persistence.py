from pathlib import Path
import joblib


def save_model(model, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, path)

    return path


def save_dataframe(df, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)

    return path


def save_predictions(predictions_df, path):
    return save_dataframe(predictions_df, path)