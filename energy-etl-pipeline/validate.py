import pandas as pd
import json
import os

def validate_data():
    file_path = "data/sample_clean.csv"

    # Make sure the CSV exists
    if not os.path.exists(file_path):
        print(f"❌ ERROR: File not found → {file_path}")
        return

    df = pd.read_csv(file_path)

    # Ensure output directory exists
    os.makedirs("data", exist_ok=True)

    # Core validation
    report = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "column_types": df.dtypes.astype(str).to_dict(),
        "missing_values_per_column": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
    }

    # Optional: Detect zero or negative values in key numeric columns
    numeric_cols = [col for col in df.columns if df[col].dtype != 'object']

    zero_neg_check = {}
    for col in numeric_cols:
        zero_neg_check[col] = {
            "zeros": int((df[col] == 0).sum()),
            "negatives": int((df[col] < 0).sum())
        }

    report["zero_negative_value_check"] = zero_neg_check

    # Save validation report
    output_path = "data/validation_report.json"
    with open(output_path, "w") as f:
        json.dump(report, f, indent=4)

    print(f"✅ Validation report saved to {output_path}")
    print(f"📌 Rows: {len(df)} | Columns: {len(df.columns)}")
    print("📌 Missing values detected:", df.isnull().sum().sum())

if __name__ == "__main__":
    validate_data()
