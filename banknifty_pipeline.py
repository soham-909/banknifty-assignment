import os
import subprocess
import pandas as pd
from datetime import datetime

# ========================
# CONFIGURATION
# ========================
DATE = "2024-01-10"
INPUT_DIR = "data/candles/BANKNIFTY/2024-01-10"
OUTPUT_DIR = "5min_candles"
RESAMPLE_INTERVAL = "5T"

S3_BUCKET = "s3://desiquant/data/candles/BANKNIFTY/2024-01-10/"
S3_HOST = "https://cbabd13f6c54798a9ec05df5b8070a6e.r2.cloudflarestorage.com"
ACCESS_KEY = "5c8ea9c516abfc78987bc98c70d2868a"
SECRET_KEY = "0cf64f9f0b64f6008cf5efe1529c6772daa7d7d0822f5db42a7c6a1e41b3cadf"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ========================
# DATA DOWNLOAD
# ========================
def download_data():
    """
    Downloads BANKNIFTY candle data using s3cmd.
    Requires s3cmd to be installed on the system.
    """
    print("⬇️ Downloading data using s3cmd...")

    command = [
        "s3cmd", "sync", S3_BUCKET, INPUT_DIR,
        "--host", S3_HOST,
        "--host-bucket", S3_HOST,
        "--access_key", ACCESS_KEY,
        "--secret_key", SECRET_KEY,
        "--region", "auto"
    ]

    subprocess.run(command, check=True)
    print(" Data download completed.\n")


# ========================
# DATA PROCESSING
# ========================
def filter_single_day(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only records for 10th Jan 2024."""
    df["date"] = pd.to_datetime(df["date"])
    return df[df["date"].dt.date == pd.to_datetime(DATE).date()]


def generate_5min_candles(df: pd.DataFrame) -> pd.DataFrame:
    """Generate 5-minute OHLC candles."""
    df = df.set_index("date")

    return (
        df.resample(RESAMPLE_INTERVAL)
        .agg({
            "open": "first",
            "high": "max",
            "low": "min",
            "close": "last",
            "volume": "sum"
        })
        .dropna()
    )


# ========================
# BONUS: FIBONACCI PIVOTS
# ========================
def calculate_fibonacci_pivots(df: pd.DataFrame, filename: str):
    """Calculate and display Fibonacci Pivot Points."""
    high = df["high"].max()
    low = df["low"].min()
    close = df["close"].iloc[-1]

    P = (high + low + close) / 3
    diff = high - low

    print(f"\n Fibonacci Pivot Points for {filename}")
    print(f"Pivot: {P:.2f}")
    print(f"R1: {P + 0.382 * diff:.2f}")
    print(f"R2: {P + 0.618 * diff:.2f}")
    print(f"R3: {P + diff:.2f}")
    print(f"S1: {P - 0.382 * diff:.2f}")
    print(f"S2: {P - 0.618 * diff:.2f}")
    print(f"S3: {P - diff:.2f}")


# ========================
# MAIN PIPELINE
# ========================
def main():
    # Step 1: Download data
    if not os.listdir(INPUT_DIR):
        download_data()

    # Step 2: Process each file
    for file in os.listdir(INPUT_DIR):
        if not file.endswith(".parquet.gz"):
            continue

        df = pd.read_parquet(os.path.join(INPUT_DIR, file))
        df = filter_single_day(df)

        if df.empty:
            continue

        candles_5min = generate_5min_candles(df)

        output_file = file.replace(".parquet.gz", "_5min.csv")
        candles_5min.to_csv(os.path.join(OUTPUT_DIR, output_file))

        # Bonus calculation
        calculate_fibonacci_pivots(df, file)

    print("\nAssignment execution completed successfully.")


if __name__ == "__main__":
    main()
