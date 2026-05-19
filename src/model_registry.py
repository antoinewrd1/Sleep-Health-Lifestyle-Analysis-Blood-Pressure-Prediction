from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

def get_model_registry(random_state=42):
    return {
        "Random Forest": RandomForestRegressor(random_state=random_state),
        "Gradient Boosting": GradientBoostingRegressor(random_state=random_state),
        "SVR": SVR()
    }

def get_parameter_grids():
    return {
        "Random Forest": {
            "model__n_estimators": [100, 200],
            "model__max_depth": [None, 5, 10],
            "model__min_samples_split": [2, 5]
        },
        "Gradient Boosting": {
            "model__n_estimators": [100, 200],
            "model__learning_rate": [0.03, 0.05, 0.10],
            "model__max_depth": [2, 3, 4]
        },
        "SVR": {
            "model__kernel": ["rbf"],
            "model__C": [1, 10],
            "model__gamma": ["scale", "auto"],
            "model_epsilon": [0.1, 0.2]
        }
    }

        