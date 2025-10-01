import requests
import json

API_URL = "https://api.eia.gov/v2/electricity/electric-power-operational-data/data/"
API_KEY = "YOUR_API_KEY"  # replace with your own

params = {
    "frequency": "monthly",
    "data": ["consumption-for-eg", "generation", "cost", "stocks"],
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "offset": 0,
    "length": 5000,
    "api_key": API_KEY
}

def extract_data():
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        with open("data/sample_raw.json", "w") as f:
            json.dump(data, f)
        print("Data extracted successfully!")
    else:
        print("Failed to extract data:", response.status_code)

if __name__ == "__main__":
    extract_data()
