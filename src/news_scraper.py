from datetime import datetime
import os
import requests
import pandas as pd

from data_cleaning import clean_news_data  # Import the cleaning function


def fetch_news(api_key):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'category': 'business',
        'language': 'en',
        'country': 'us',
        'apiKey': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

        # Process and clean the news data
        news_data = [{'Source': article['source']['name'], 'Title': article['title'], 'Author': article.get('author'),
                      'Description': article.get('description'), 'URL': article['url'],
                      'Published At': article['publishedAt'],
                      'Content': article.get('content')} for article in articles]

        # Clean the data
        cleaned_news_data = clean_news_data(news_data)

        today = datetime.now().strftime('%Y-%m-%d')

        # Define the file path with the current date
        project_root = os.path.dirname(os.path.dirname(__file__))
        data_dir = os.path.join(project_root, 'data')

        # Ensure the data directory exists
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Create the unique filename with the current date
        output_file = os.path.join(data_dir, f'news_data_{today}.csv')

        # Save the cleaned data to the CSV file
        cleaned_news_data.to_csv(output_file, index=False)
        print(f"Cleaned news data saved to '{output_file}'")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")



