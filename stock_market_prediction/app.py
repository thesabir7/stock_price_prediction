import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/AAPL.csv")

# Preprocess
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df['Prediction'] = df[['Close']].shift(-30)

# Features and labels
X = df[['Close']][:-30].values
y = df['Prediction'][:-30].values

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# Forecast next 30 days
X_forecast = df[['Close']][-30:].values
forecast_prediction = model.predict(X_forecast)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df.index[-60:], df['Close'][-60:], label='Actual')
plt.plot(df.index[-30:], forecast_prediction, label='Predicted', linestyle='--')
plt.title("Stock Price Forecast (Next 30 Days)")
plt.xlabel("Date")
plt.ylabel("Close Price USD")
plt.legend()
plt.grid(True)
plt.show()
