# 9. FINAL TEST SET EVALUATION

test_results = []

for name, model in best_models.items():
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    test_results.append({
    "Model": name,
    "Test MAE": mae,
    "Test MSE": mse,
    "Test RMSE": rmse,
    "Test R2": r2
    })

test_results_df = pd.DataFrame(test_results).sort_values(by="Test RMSE")

print("\nFinal Test Results:")
print(test_results_df)