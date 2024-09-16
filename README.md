# Web Scraper Bot

A Python-based web scraping bot that collects data from websites, including **business news headlines** from NewsAPI and **stock prices** from Alpha Vantage. The bot then compiles the data into HTML and PDF reports, which are saved with unique filenames based on the current date.

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Automation with Scheduler](#automation-with-scheduler)
- [License](#license)

---

## Features

- **Scrape Business News**: Fetches business-related news headlines using the **NewsAPI**.
- **Scrape Stock Data**: Fetches stock market data for a given symbol (e.g., AAPL) using **Alpha Vantage**.
- **Generate Reports**: Compiles the scraped data into both **HTML** and **PDF** reports, with daily unique filenames.
- **Automated Execution**: Schedules the script to run automatically at specified intervals using the `schedule` library.
- **Secure API Keys**: Hides API keys by loading them from environment variables or `.env` files.

---

## Technologies Used

- **Python**: The core language for the bot.
- **Jinja2**: For templating HTML reports.
- **WeasyPrint**: (optional) For converting HTML reports to PDFs.
- **pandas**: For handling and cleaning data.
- **schedule**: For scheduling script execution.
- **dotenv**: For loading environment variables from a `.env` file.

---

## Project Structure

```plaintext
Web Scraper Bot/
│
├── data/                   # Directory for storing scraped data (CSV files)
│   ├── news_data_YYYY-MM-DD.csv       # Daily business news data
│   └── AAPL_stock_data_YYYY-MM-DD.csv # Daily stock data for AAPL
│
├── reports/                # Directory for storing generated reports
│   ├── report_YYYY-MM-DD.html         # Daily HTML report
│   └── report_YYYY-MM-DD.pdf          # Daily PDF report (if using WeasyPrint)
│
├── src/                    # Source code directory
│   ├── news_scraper.py             # Script to fetch and clean news data
│   ├── stock_scraper.py            # Script to fetch and clean stock data
│   ├── report_generator.py         # Script to generate HTML and PDF reports
│   ├── scheduler.py                # Main automation script
│   └── data_cleaning.py            # Functions for cleaning data
│
├── templates/              # Jinja2 HTML template for reports
│   └── report_template.html
│
├── .env                    # Environment file for API keys (not committed to Git)
├── .gitignore              # Git ignore file (to ignore .env, etc.)
├── venv/                   # Python virtual environment (not committed to Git)
├── README.md               # This README file
└── requirements.txt        # Python dependencies

