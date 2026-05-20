from src.evaluation import evaluate_regression_model

def test_evaluate_regression_model_returns_expected_metrics():
	y_true = [100, 120, 140]
	y_pred = [100, 115, 150]

	metrics = evaluate_regression_model(y_true, y_pred)

	assert "mae" in metrics
	assert "rmse" in metrics
	assert "r2" in metrics