from src.schema import REQUIRED_COLUMNS, NUMERIC_RANGE_RULES


def test_required_columns_contains_blood_pressure():
    assert "Blood Pressure" in REQUIRED_COLUMNS


def test_numeric_range_rules_contains_sleep_duration():
    assert "Sleep Duration" in NUMERIC_RANGE_RULES


def test_stress_level_range_is_valid():
    minimum, maximum = NUMERIC_RANGE_RULES["Stress Level"]

    assert minimum == 1
    assert maximum == 10