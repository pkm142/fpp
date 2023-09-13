from flask import Flask, jsonify
import pandas as pd
import numpy as np
import statsmodels.api as sm

app = Flask(__name__)

# Load your dataset
data = pd.read_csv('fpp.csv')

# Data preprocessing
data['Month'] = pd.to_datetime(data['Month'], format='%b-%y')
data.set_index('Month', inplace=True)

# Splitting the data into training and testing sets
train_size = int(len(data) * 0.8)  # 80% for training, 20% for testing
train_data = data[:train_size]
test_data = data[train_size:]

# Create and fit an ARIMA model (modify p, d, and q)
p, d, q = (1, 1, 1)  # Example values, tune these based on your data
model = sm.tsa.ARIMA(train_data['Price'], order=(p, d, q))
results = model.fit()

# Define a route to get predictions
@app.route('/get_predictions', methods=['GET'])
def get_predictions():
    # Make predictions for the next month
    n_forecast = 1  # You can change this to forecast more months ahead
    forecast = results.forecast(steps=n_forecast)

    # Calculate the expected percentage change from the last month
    last_month_price = test_data['Price'].iloc[-1]
    expected_percentage_change = ((forecast[0] - last_month_price) / last_month_price) * 100

    # Create a dictionary to store the results
    result = {
        "predicted_price": float(forecast[0]),
        "expected_percentage_change": float(expected_percentage_change)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
