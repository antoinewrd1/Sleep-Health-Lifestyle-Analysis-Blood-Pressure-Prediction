from pathlib import Path
import pandas as pd

def load_data(file_path):
	filePath = Path(
    	r"C:\Users\antoi\Downloads\archive (3)\Sleep_Health_and_Lifestyle_Dataset.csv"
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