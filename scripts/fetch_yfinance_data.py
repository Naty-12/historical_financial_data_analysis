import yfinance as yf
import pandas as pd
import os
import datetime

# Parameters
tickers = ['TSLA', 'BND', 'SPY']
start_date = '2015-07-01'
end_date = datetime.datetime.today().strftime('%Y-%m-%d')
data_dir = 'data'

# Create data directory if it doesn't exist
os.makedirs(data_dir, exist_ok=True)

# Download and save
for ticker in tickers:
    try:
        df = yf.download(ticker, start=start_date, end=end_date)
        if df.empty:
            print(f"[WARNING] No data found for {ticker}. Skipping.")
        else:
            df.to_csv(f"{data_dir}/{ticker}.csv")
            print(f"Saved {ticker} data to {data_dir}/{ticker}.csv")
    except Exception as e:
        print(f"[ERROR] Failed to download {ticker}: {e}")