# 2. DATA QUALITY CHECKS

def validate_target_column(df, target_column):
	if target_column not in df.columns:
		raise ValueError(
			f"Target column '{target_column}' was not created successfully."
)


def print_column_names(df):
	print("Column Names:")
	print(df.columns.tolist())

def print_missing_values(df):
	print("\nMissing Values:")
	print(df.isnull().sum())

def print_duplicate_rows(df):
	print("\nDuplicate Rows:")
	print(df.duplicated().sum())

def print_data_types(df):
	print("\nData Types:")
	print(df.dtypes)

def run_data_quality_checks(df):
	print_column_names(df)
	print_missing_values(df)
	print_duplicate_rows(df)
	print_data_types(df)