import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.pipelines import(
	identify_feature_types,
	build_preprocessor
)


def test_identify_feature_types_separates_numeric_and_categorical_columns():
	X  = pd.DataFrame(
		{
			"Age": [30, 45],
			"Sleep Duration": [7.5, 6.0],
			"Gender": ["Male", "Female"],
			"BMI Category": ["Normal", "Overweight"]
		}
	)

	numeric_features, categorical_features = identify_feature_types(X)

	assert "Age" in numeric_features
	assert "Sleep Duration" in numeric_features
	assert "Gender" in categorical_features
	assert "BMI Category" in categorical_features

def test_build_preprocessor_returns_columns_transformer():
	numeric_features = ["Age", "Sleep Duration"]
	categorical_features = ["Gender",  "BMI Category"]

	preprocessor = build_preprocessor(
		numeric_features,
		categorical_features
	)

	assert isinstance(preprocessor, ColumnTransformer)

def test_build_preprocessor_can_fit_transform_sample_data():
	X = pd.DataFrame(
		{
			"Age": [30, 45, np.nan],
			"Sleep Duration": [7.5, 6.0, 8.0],
			"Gender": ["Male", "Female", "Male"],
			"BMI Category": ["Normal", "Overweight", np.nan]
		}
	)

	numeric_features, categorical_features = identify_feature_types(X)

	preprocessor = build_preprocessor(
		numeric_features,
		categorical_features
	)

	transformed = preprocessor.fit_transform(X)

	assert transformed.shape[0] == 3
	assert transformed.shape[1] >= 4