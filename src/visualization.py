# 10. PREDICTION PLOTS

def actual_vs_predicted(y_true, y_pred, title):
    plt.figure(figsize=(8,5))
    plt.scatter(y_true, y_pred, alpha=0.70)
    plt.plot(
    [y_true.min(), y_true.max()],
    [y_true.min(), y_true.max()],
    linestyle="--"
    )
    plt.xlabel("Actual Systolic BP")
    plt.ylabel("Predicted Systolic BP")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def residual_plot(y_true, y_pred, title):
    residuals = y_true - y_pred

    plt.figure(figsize=(8,5))
    plt.scatter(y_pred, residuals, alpha=0.70)
    plt.axhline(0, linestyle="--")
    plt.xlabel("Predicted Systolic BP")
    plt.ylabel("Residuals")
    plt.title(title)
    plt.tight_layout()
    plt.show()


for name, model in best_models.items():
    predictions = model.predict(X_test)

    actual_vs_predicted(
        y_test,
        predictions,
        f"{name}: Actual vs Predicted"
    )

    residual_plot(
        y_test,
        predictions,
        f"{name}: Residual Plot"
    )

# 11. FEATURE IMPORTANCE: TREE MODELS

def get_feature_names(preprocessor):

    feature_names = []

    if numericFeatures:
        feature_names.extend(numericFeatures)

    if categoricalFeatures:
        encoder = (
            preprocessor
            .named_transformers_["categorical"]
            .named_steps["encoder"]
                )

        encoded_features = encoder.get_feature_names_out(categoricalFeatures)
        feature_names.extend(encoded_features)

    return feature_names

for name in ["Random Forest", "Gradient Boosting"]:
    if name in best_models:
        model = best_models[name]
        fitted_preprocessor = model.named_steps["preprocessor"]
        fitted_estimator = model.named_steps["model"]

        feature_names = get_feature_names(fitted_preprocessor)

        importance = pd.Series(
        fitted_estimator.feature_importances_,
        index=feature_names
        ).sort_values(ascending=False)

        print(f"\nTop 10 Features for {name}:")
        print(importance.head(10))

        plt.figure(figsize=(9,5))
        importance.head(10).sort_values().plot(kind="barh")
        plt.title(f"Top 10 Feature Importances: {name}")
        plt.xlabel("Importances")
        plt.tight_layout()
        plt.show()

# 12. MODEL COMPARISON CHARTS

plt.figure(figsize=(8, 5))
sns.barplot(data=test_results_df, x="Model", y="Test RMSE")
plt.title("Model Comparison by Test RMSE")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=test_results_df, x="Model", y="Test R2")
plt.title("Model Comparison by Test R2")
plt.tight_layout
plt.show()