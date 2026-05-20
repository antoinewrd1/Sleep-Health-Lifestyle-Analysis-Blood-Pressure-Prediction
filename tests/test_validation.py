import pytest
import pandas as pd

from src.validation import validate_numeric_ranges


def test_validate_numeric_ranges_detects_invalid_values():
    df = pd.DataFrame(
        {
            "Age": [35, 150],
        }
    )

    range_rules = {
        "Age": (18, 100),
    }

    with pytest.raises(ValueError):
        validate_numeric_ranges(df, range_rules)