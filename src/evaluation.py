import numpy as np
import pandas as pd

from sklearn.metrics import(
	mean_absolute_error,
	mean_squared_error,
	r2_score
)

def evaluate_regression_model(y_true, y_pred):
	mse = mean_squared_error(y_true, y_pred)

	return {
		"mae": mean_absolute_error(y_true, y_pred),
		"rmse": np.sqrt(mse),
		"r2": r2_score(y_true, y_pred)
		}

def evaluate_models(best_models, X_test, y_test):
	test_results = []

	for name, model in best_models.items():
		predictions = model.predict(X_test)

		mse = mean_squared_error(y_test, predictions)

		test_results.append(
			{
				"Model": name,
				"Test MAE": mean_absolute_error(y_test, predictions),
				"Test MSE": mse,
				"Test RMSE": np.sqrt(mse),
				"Test R2": r2_score(y_test, predictions)
			}
		)

	return pd.DataFrame(test_results).sort_values(by="Test RMSE")