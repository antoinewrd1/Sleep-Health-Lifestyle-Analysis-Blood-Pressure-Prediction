import os
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split, KFold, cross_validate, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.exceptions import ConvergenceWarning
from pathlib import Path
from src.validation import (validate_target_column, run_data_quality_checks)
from src.data_loader import load_data
from src.feature_engineering import (prepare_features, separate_features_target)

DATA_PATH = "data/Sleep_Health_and_Lifestyle_Dataset.csv"


trget = "Systolic"

DROP_COLUMNS = [
	"Systolic",
	"Diastolic"
]

df = load_data(DATA_PATH)

run_data_quality_checks(df)

df = prepare_features(df)

validate_target_column(df, trget)

X, y = separate_features_target(
	df,
	trget,
	DROP_COLUMNS,
)