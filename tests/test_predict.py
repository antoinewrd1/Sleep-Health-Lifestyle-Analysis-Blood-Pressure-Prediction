import pandas as pd
import joblib

from sklearn.dummy import DummyRegressor

from src.predict import load_model


def test_load_model_loads_joblib_file(tmp_path):
    model = DummyRegressor(strategy="mean")

    model_path = tmp_path / "model.joblib"

    joblib.dump(model, model_path)

    loaded_model = load_model(model_path)

    assert isinstance(loaded_model, DummyRegressor)