import pandas as pd
import pytest

from src.validation import validate_required_columns, validate_blood_pressure_format

def test_validate_required_columns_detects_missing_column():
    df = pd.DataFrame({"Age": [30]})

    with pytest.raises(ValueError):
        validate_required_columns(df, ["Age", "Blood Pressure"])

def test_validate_blood_pressure_format_rejects_invalid_format():
    df = pd.DataFrame({"Blood Pressure": ["120-80"]})

    with pytest.raises(ValueError):
        validate_blood_pressure_format(df)