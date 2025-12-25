# BankNifty 5-Minute Candle Generation

## Objective
Generate 5-minute OHLC candles for BankNifty strike-price data for **10th January 2024** and share the solution via a GitHub repository.

## Approach
- Raw data files contain multi-day OHLC candle data.
- Data is first filtered to include **only 10th Jan 2024**.
- Candles are aggregated into **5-minute intervals** using standard OHLC rules:
  - Open: First value in the time window
  - High: Maximum value in the time window
  - Low: Minimum value in the time window
  - Close: Last value in the time window

## Output
- 5-minute candles are saved as CSV files in the `5min_candles` folder.
- The same logic is applied to **all strike-price files**.

## Bonus Feature: Fibonacci Pivot Points
- Fibonacci Pivot Points are calculated for the entire trading day (10th Jan 2024).
- The following levels are computed using daily High, Low, and Close:
  - Pivot (P)
  - Resistance levels: R1, R2, R3
  - Support levels: S1, S2, S3
- Bonus logic is implemented in `bonus_fibonacci_pivot.py`.

## Tech Stack
- Python
- Pandas
- Parquet (pyarrow)
