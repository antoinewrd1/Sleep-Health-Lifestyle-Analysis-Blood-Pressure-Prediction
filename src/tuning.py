# 8. HYPERPARAMETER TUNING

parameter_grids = {
    "Random Forest": {
        "model__n_estimators": [100, 200, 300],
        "model__max_depth": [None, 5, 10],
        "model__min_samples_split": [2, 5],
        "model__min_samples_leaf": [1, 2]
    },

       "Gradient Boosting": {
        "model__n_estimators": [100, 200],
        "model__learning_rate": [0.03, 0.05, 0.10],
        "model__max_depth": [2, 3, 4],
    },

       "SVR": {
        "model__kernel": ["rbf"],
        "model__C": [1, 10, 100],
        "model__gamma": ["scale", "auto"],
        "model__epsilon": [0.1, 0.2, 0.5]
    }
}


best_models = {}

for name, model in models.items():
    print(f"\nTuning {name}...")

    grid = GridSearchCV(
        estimator=model,
        param_grid = parameter_grids[name],
        cv=cross_validation,
        scoring="neg_root_mean_squared_error",
        n_jobs=-1
    )

    grid.fit(X_train, y_train)

    best_models[name] = grid.best_estimator_

    print(f"Best Parameters for {name}:")
    print(grid.best_params_)
    print(f"Best CV RMSE: {-grid.best_score_:.4f}")
    
    
        


