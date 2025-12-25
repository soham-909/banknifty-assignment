
import os
import pandas as pd

INPUT_DIR = "/content/data/candles/BANKNIFTY/2024-01-10"
OUTPUT_DIR = "5min_candles"
DATE = "2024-01-10"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    if not file.endswith(".parquet.gz"):
        continue

    df = pd.read_parquet(os.path.join(INPUT_DIR, file))
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["date"].dt.date == pd.to_datetime(DATE).date()]

    df.set_index("date", inplace=True)

    candles = df.resample("5T").agg({
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        "volume": "sum"
    }).dropna()

    candles.to_csv(
        os.path.join(OUTPUT_DIR, file.replace(".parquet.gz", "_5min.csv"))
    )

print("Done")
