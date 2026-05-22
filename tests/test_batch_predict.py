import joblib
import pandas as pd

from sklearn.dummy import DummyRegressor

from src.batch_predict import run_batch_predictions


def test_run_batch_predictions_creates_output_file(tmp_path):
    X_train = pd.DataFrame(
        {
            "Age": [30, 40, 50],
        }
    )

    y_train = [110, 120, 130]

    model = DummyRegressor(strategy="mean")
    model.fit(X_train, y_train)

    model_path = tmp_path / "model.joblib"
    input_path = tmp_path / "input.csv"
    output_path = tmp_path / "predictions.csv"

    joblib.dump(model, model_path)

    pd.DataFrame({"Age": [35, 45]}).to_csv(input_path, index=False)

    result = run_batch_predictions(
        model_path=model_path,
        input_csv_path=input_path,
        output_csv_path=output_path,
    )

    assert output_path.exists()
    assert "predicted_systolic_bp" in result.columns