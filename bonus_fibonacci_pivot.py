
import os
import pandas as pd

INPUT_DIR = "data/candles/BANKNIFTY/2024-01-10"
DATE = "2024-01-10"

for file in os.listdir(INPUT_DIR):
    if not file.endswith(".parquet.gz"):
        continue

    df = pd.read_parquet(os.path.join(INPUT_DIR, file))
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["date"].dt.date == pd.to_datetime(DATE).date()]

    if df.empty:
        continue

    high = df["high"].max()
    low = df["low"].min()
    close = df["close"].iloc[-1]

    P = (high + low + close) / 3

    print(f"\nFibonacci Pivot Points for {file}")
    print(f"Pivot: {P:.2f}")
    print(f"R1: {P + 0.382*(high-low):.2f}")
    print(f"R2: {P + 0.618*(high-low):.2f}")
    print(f"R3: {P + (high-low):.2f}")
    print(f"S1: {P - 0.382*(high-low):.2f}")
    print(f"S2: {P - 0.618*(high-low):.2f}")
    print(f"S3: {P - (high-low):.2f}")
