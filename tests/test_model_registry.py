from src.model_registry import (
    get_model_registry,
    get_parameter_grids,
)


def test_get_model_registry_contains_expected_models():
    models = get_model_registry(random_state=42)

    assert "Random Forest" in models
    assert "Gradient Boosting" in models
    assert "SVR" in models


def test_get_parameter_grids_contains_expected_models():
    grids = get_parameter_grids()

    assert "Random Forest" in grids
    assert "Gradient Boosting" in grids
    assert "SVR" in grids


def test_parameter_grid_uses_pipeline_model_prefix():
    grids = get_parameter_grids()

    for grid in grids.values():
        for parameter_name in grid:
            assert parameter_name.startswith("model__")