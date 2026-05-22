import joblib
import pandas as pd

from sklearn.dummy import DummyRegressor

from src.services.model_serving_service import ModelServingService


def test_model_serving_service_predicts_dataframe(tmp_path):
    X = pd.DataFrame({"Age": [30, 40, 50]})
    y = [110, 120, 130]

    model = DummyRegressor(strategy="mean")
    model.fit(X, y)

    model_path = tmp_path / "model.joblib"
    joblib.dump(model, model_path)

    service = ModelServingService(model_path=model_path)

    predictions = service.predict_dataframe(pd.DataFrame({"Age": [35]}))

    assert len(predictions) == 1