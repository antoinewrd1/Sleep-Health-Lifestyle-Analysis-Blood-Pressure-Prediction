from pathlib import Path


def generate_data_profile(df, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    profile = {
        "row_count": int(df.shape[0]),
        "column_count": int(df.shape[1]),
        "columns": df.columns.tolist(),
        "missing_values": df.isna().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
    }

    output_path.write_text(str(profile), encoding="utf-8")

    return profile