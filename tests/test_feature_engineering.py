import pandas as pd

from src.feature_engineering import prepare_features

def test_prepare_features_creates_systolic_and_diastolic():
    df = pd.DataFrame({
        "Blood Pressure": ["120/80"],
        "Sleep Disorder": [None],
    })

    result = prepare_features(df)

    assert "Systolic" in result.columns
    assert "Diastolic" in result.columns
    assert result.loc[0, "Systolic"] == 120
    assert result.loc[0, "Diastolic"] == 80
    assert result.loc[0, "Sleep Disorder"] == "No Disorder"