import pandas as pd
import json

def validate_data():
    df = pd.read_csv("data/sample_clean.csv")
    report = {
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "rows": len(df)
    }

    with open("data/validation_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Validation report saved to data/validation_report.json")

if __name__ == "__main__":
    validate_data()
