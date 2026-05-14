from sklearn.model_selection import (train_test_split, cross_val_score, GridSearchCV)

# 7. CROSS VALIDATION

cross_validation = KFold(n_splits=5, shuffle=True, random_state=42)

cv_results = []

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

for name, model in models.items():
    scores = cross_validate(
        model,
        X_train,
        y_train,
        cv=cross_validation,
        scoring={
            "MAE": "neg_mean_absolute_error",
            "MSE": "neg_mean_squared_error",
            "R2": "r2"
        },
        return_train_score=False
    )

    cv_results.append({
        "Model": name,
        "CV MAE": -scores["test_MAE"].mean(),
        "CV MSE": -scores["test_MSE"].mean(),
        "CV RMSE": np.sqrt(-scores["test_MSE"].mean()),
        "CV R2": scores["test_R2"].mean()
    })

cv_results_df = pd.DataFrame(cv_results).sort_values(by="CV RMSE")

print("\nCross-Validation Results:")
print(cv_results_df)