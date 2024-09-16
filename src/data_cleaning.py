import pandas as pd

# Function to clean the news data
def clean_news_data(news_data):
    """
    Cleans and organizes the news data fetched from NewsAPI.
    - Removes rows with missing headlines.
    - Fills missing values in non-critical columns (e.g., 'Author', 'Description').
    - Drops duplicates based on the headline.
    """
    df_news = pd.DataFrame(news_data)

    # Remove rows where the headline is missing (essential column)
    df_news = df_news.dropna(subset=['Title'])

    # Fill missing values in other columns with default values
    df_news['Author'] = df_news['Author'].fillna('Unknown')
    df_news['Description'] = df_news['Description'].fillna('No description available')
    df_news['Content'] = df_news['Content'].fillna('Content not available')

    # Remove duplicates based on the title (to ensure unique articles)
    df_news = df_news.drop_duplicates(subset=['Title'], keep='first')

    # Organize columns and rename for clarity
    df_news = df_news[['Source', 'Title', 'Author', 'Description', 'URL', 'Published At', 'Content']]

    # Sort by the published date
    df_news = df_news.sort_values(by='Published At', ascending=False)

    # Reset index for cleaner display
    df_news = df_news.reset_index(drop=True)

    return df_news

# Function to clean the stock data
def clean_stock_data(stock_data):
    """
    Cleans and organizes stock data fetched from Alpha Vantage.
    - Converts columns to the correct data types.
    - Drops unnecessary columns if needed.
    - Sorts data by date in descending order.
    """
    df_stock = pd.DataFrame(stock_data)

    # Convert numeric columns from strings to floats
    numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df_stock[numeric_columns] = df_stock[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # Handle missing values (if any): here we'll drop rows where key columns are missing
    df_stock = df_stock.dropna(subset=numeric_columns)

    # Sort by date in descending order
    df_stock['Date'] = pd.to_datetime(df_stock['Date'])
    df_stock = df_stock.sort_values(by='Date', ascending=False)

    # Reset the index for clean display
    df_stock = df_stock.reset_index(drop=True)

    return df_stock
