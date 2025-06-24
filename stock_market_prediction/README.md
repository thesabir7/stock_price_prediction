# 📈 Stock Market Prediction

A machine learning project to forecast stock market closing prices using historical data and linear regression.

## Features

- Predicts future closing prices based on past trends.
- Visualizes actual vs predicted prices.
- Download data directly using Yahoo Finance API.

## How to Run

```bash
git clone <repo-url>
cd stock_market_prediction
pip install -r requirements.txt
python -c "from stock_utils import download_data; download_data()"
python app.py
```

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Matplotlib
- yFinance
