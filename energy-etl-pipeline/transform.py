import pandas as pd
import json
import os

def transform_data():
    file_path = "data/sample_raw.json"

    # 1. Check file exists
    if not os.path.exists(file_path):
        print(f"❌ ERROR: File not found → {file_path}")
        return

    # 2. Load JSON
    with open(file_path, "r") as f:
        raw = json.load(f)

    # 3. Extract dataset
    records = raw.get("response", {}).get("data", [])

    if len(records) == 0:
        print("❌ ERROR: No data found in JSON under response['data']")
        return

    df = pd.DataFrame(records)

    # 4. Clean column names
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]

    # 5. Convert numeric columns safely
    numeric_cols = ["cost", "generation", "consumption_for_eg", "stocks"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")  # convert safely

    # 6. Create derived feature safely
    if "cost" in df.columns and "generation" in df.columns:
        df["cost_per_mwh"] = df["cost"] / df["generation"].replace({0: pd.NA})
    else:
        print("⚠️ cost_per_mwh NOT created (required columns missing)")

    # 7. Save output CSV
    out_path = "data/sample_clean.csv"
    df.to_csv(out_path, index=False)

    print(f"✅ Data transformed and saved to {out_path}")
    print("📌 Rows:", len(df))
    print("📌 Columns:", len(df.columns))

if __name__ == "__main__":
    transform_data()
