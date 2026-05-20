from pathlib import Path
import pandas as pd

def load_data(file_path):
	filePath = Path(
    	r"C:\Users\antoi\Repos\Sleep-Health-Lifestyle-Analysis-Blood-Pressure-Prediction\Sleep_Health_and_Lifestyle_Dataset.csv"
	)

	if not filePath.exists():
    		raise FileNotFoundError(
        		f"The dataset was not found at :\n{filePath}"
    	)

	df = pd.read_csv(filePath)

	print(f"Dataset Shape: {df.shape}")
	print("\nFirst 10 Rows:")
	print(df.head(10))
	print("The data has loaded successfully.")

	return df