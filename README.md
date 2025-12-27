## BANKNIFTY Intraday Candle Processing Assignment

This repository contains a complete and reproducible solution for processing BANKNIFTY intraday candle data as per the given assignment requirements.

The project demonstrates:

Clean data handling

Time-based resampling

Technical level calculation

Simple analytical comparison on generated candles

## Features Implemented
 Core Requirements

Download intraday candle data using s3cmd (as per assignment instructions)

Filter data for 10th January 2024

Generate 5-minute OHLC candles for each strike-price file

Save generated candles as CSV files in a separate folder

Process all files in the given directory

## Bonus Feature

Calculate Fibonacci Pivot Points for the entire trading day

Display the following levels in console output:

Pivot

R1, R2, R3

S1, S2, S3

## Additional Analytical Check

Access the generated 5-minute candle at 10:30

Compare its High value with the immediately preceding candle

Print whether the High is:

INCREASING

DECREASING

UNCHANGED

No new column is added; output is displayed only in the console
