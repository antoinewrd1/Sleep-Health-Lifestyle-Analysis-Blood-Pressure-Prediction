from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

numericFeatures = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categoricalFeatures = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

numericPipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)

categoricalPipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]
)


preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numericPipeline, numericFeatures),
        ("categorical", categoricalPipeline, categoricalFeatures)
    ]
)

# 6. MODEL PIPELINES

models = {
    "Random Forest": Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", RandomForestRegressor(random_state=42))
        ]
    ),

    "Gradient Boosting": Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", GradientBoostingRegressor(random_state=42))
        ]
    ),

    "SVR": Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", SVR())
        ]
    ),
}
