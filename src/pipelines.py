from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

def identify_feature_types(X):
	numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

	categorical_features = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

	return numeric_features, categorical_features

def build_preprocessor(numeric_features, categorical_features):

	numeric_pipeline = Pipeline(
    		steps=[
        		("imputer", SimpleImputer(strategy="median")),
        		("scaler", StandardScaler())
    		]
	)

	categorical_pipeline = Pipeline(
    		steps=[
        		("imputer", SimpleImputer(strategy="most_frequent")),
        		("encoder", OneHotEncoder(handle_unknown="ignore"))
    		]
	)


	return ColumnTransformer(
    		transformers=[
        		("numeric", numeric_pipeline, numeric_features),
        		("categorical", categorical_pipeline, categorical_features)
    		]
	)

