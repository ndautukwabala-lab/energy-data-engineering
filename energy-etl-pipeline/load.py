import pandas as pd
from sqlalchemy import create_engine

def load_data():
    df = pd.read_csv("data/sample_clean.csv")

    engine = create_engine("sqlite:///energy.db")
    df.to_sql("energy_data", engine, if_exists="replace", index=False)

    print("Data loaded into SQLite database energy.db")

if __name__ == "__main__":
    load_data()
