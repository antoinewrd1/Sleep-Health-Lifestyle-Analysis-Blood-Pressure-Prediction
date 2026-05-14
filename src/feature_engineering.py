# 3. FEATURE ENGINEERING
def prepare_features(df):
	df = df.copy()

	if "Blood Pressure" in df.columns:
    		df[["Systolic", "Diastolic"]] = (
        		df["Blood Pressure"]
        		.astype(str)
        		.str.split("/", expand=True)
        		.astype(int)
    	)

    		df = df.drop(columns=["Blood Pressure"])


	if "Sleep Disorder" in df.columns:
    		df["Sleep Disorder"] = (
			df["Sleep Disorder"]
			.fillna("No Disorder")
		)

	return df

def separate_features_target(
	df,
	trget,
	DROP_COLUMNS
):
	X = df.drop(columns=DROP_COLUMNS)

	y = df[trget]
	
	return X, y