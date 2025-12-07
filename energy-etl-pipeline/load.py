import pandas as pd
import json
from sqlalchemy import create_engine

def load_data():
    file_path = "/content/data/sample_raw.json"

    # Load JSON
    with open(file_path, "r") as f:
        raw = json.load(f)

    # Extract the actual table data
    records = raw["response"]["data"]

    # Convert to DataFrame
    df = pd.DataFrame(records)

    # Load into SQLite
    engine = create_engine("sqlite:///energy.db")
    df.to_sql("energy_data", engine, if_exists="replace", index=False)

    print("✅ Data loaded into SQLite database energy.db")
    print("📌 Rows loaded:", len(df))

if __name__ == "__main__":
    load_data()
