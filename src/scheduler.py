import os
import time
import schedule
from news_scraper import fetch_news
from stock_scraper import fetch_stock_data
from report_generator import main as generate_report
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Replace with your actual API keys
API_KEY_NEWS = os.getenv('NEWS_API_KEY')
API_KEY_STOCK = os.getenv('ALPHA_VANTAGE_KEY')
STOCK_SYMBOL = 'AAPL'

def job():
    print("Starting the scheduled job...")

    # Step 1: Fetch the latest news data
    fetch_news(API_KEY_NEWS)

    # Step 2: Fetch the latest stock data
    fetch_stock_data(API_KEY_STOCK, STOCK_SYMBOL)

    # Step 3: Generate the report (HTML + PDF)
    generate_report()

    print("Scheduled job completed.")

# Schedule the job to run daily at 8 AM
schedule.every().day.at("08:00").do(job)

# Alternatively, you can schedule the job to run every hour
# schedule.every().hour.do(job)

# Keep the script running to check and run the scheduled tasks
if __name__ == '__main__':
    print("Scheduler is running...")

    # Execute the first job immediately when the script starts
    job()

    while True:
        # Run pending scheduled tasks
        schedule.run_pending()

        # Sleep for 1 minute before checking the schedule again
        time.sleep(60)
