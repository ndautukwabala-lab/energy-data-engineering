import pandas as pd
import json

def transform_data():
    with open("data/sample_raw.json") as f:
        raw = json.load(f)

    df = pd.DataFrame(raw['response']['data'])
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]

    # Derived features
    if 'cost' in df.columns and 'generation' in df.columns:
        df['cost_per_mwh'] = df['cost'].astype(float) / df['generation'].astype(float)

    df.to_csv("data/sample_clean.csv", index=False)
    print("Data transformed and saved to data/sample_clean.csv")

if __name__ == "__main__":
    transform_data()
