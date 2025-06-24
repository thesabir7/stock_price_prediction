import yfinance as yf

def download_data(ticker='AAPL', start='2010-01-01', end='2023-12-31', filename='data/AAPL.csv'):
    df = yf.download(ticker, start=start, end=end)
    df.to_csv(filename)
    print(f"{ticker} data saved to {filename}")
