def validate_target_column(df, target_column):
	if target_column not in df.columns:
		raise ValueError(
			f"Target column '{target_column}' was not created successfully."
)

def validate_required_columns(df, required_columns):
    missing = [column for column in required_columns if column not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return True

def validate_blood_pressure_format(df):
    if "Blood Pressure" not in df.columns:
        return True

    valid_format = (
        df["Blood Pressure"]
        .astype(str)
        .str.match(r"^\d+/\d+$"))

    if not valid_format.all():
        raise ValueError("Invalid blood pressure format detected.")

    return True

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


def validate_numeric_ranges(df, range_rules):
    violations = {}

    for column, (minimum, maximum) in range_rules.items():
        if column in df.columns:
            invalid_count = (
                (df[column] < minimum) |
                (df[column] > maximum)
            ).sum()

            if invalid_count > 0:
                violations[column] = int(invalid_count)

        if violations:
            raise ValueError(f"Numeric range violations detected: {violations}")

        return True