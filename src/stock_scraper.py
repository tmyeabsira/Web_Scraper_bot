from datetime import datetime
import os
import requests
import pandas as pd
from data_cleaning import clean_stock_data  # Import the cleaning function


def fetch_stock_data(api_key, symbol):
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'outputsize': 'compact',
        'datatype': 'json',
        'apikey': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        time_series = data.get('Time Series (Daily)', {})

        # Process and clean the stock data
        stock_data = [{'Date': date, 'Open': daily_data['1. open'], 'High': daily_data['2. high'],
                       'Low': daily_data['3. low'], 'Close': daily_data['4. close'],
                       'Volume': daily_data['5. volume']} for date, daily_data in time_series.items()]

        # Clean the data
        cleaned_stock_data = clean_stock_data(stock_data)

        today = datetime.now().strftime('%Y-%m-%d')

        # Define the file path with the current date
        project_root = os.path.dirname(os.path.dirname(__file__))
        data_dir = os.path.join(project_root, 'data')

        # Ensure the data directory exists
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Create the unique filename with the current date
        output_file = os.path.join(data_dir, f'{symbol}_stock_data_{today}.csv')

        # Save the cleaned stock data to the CSV file
        cleaned_stock_data.to_csv(output_file, index=False)
        print(f"Cleaned stock data for {symbol} saved to '{output_file}'")
    else:
        print(f"Failed to fetch stock data. Status code: {response.status_code}")


if __name__ == '__main__':
    api_key = 'A00GPWSIIV03BALL'
    fetch_stock_data(api_key, 'AAPL')
