from datetime import datetime

import pandas as pd
from jinja2 import Environment, FileSystemLoader
# from weasyprint import HTML


today = datetime.now().strftime('%Y-%m-%d')

# Paths to templates and output
TEMPLATES_DIR = '../templates'
OUTPUT_HTML = f'../reports/report_{today}.html'
OUTPUT_PDF = f'../reports/report_{today}.pdf'



def load_data():
    # Load cleaned data from CSVs
    news_data = pd.read_csv(f'../data/news_data_{today}.csv').to_dict(orient='records')
    stock_data = pd.read_csv(f'../data/AAPL_stock_data_{today}.csv').to_dict(orient='records')

    return news_data, stock_data


def generate_html_report(news_data, stock_data):
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template('report_template.html')

    # Render the template with news and stock data
    html_content = template.render(news_data=news_data, stock_data=stock_data)

    # Save the rendered HTML to file
    with open(OUTPUT_HTML, 'w') as f:
        f.write(html_content)

    print(f"HTML report saved to {OUTPUT_HTML}")
    return html_content


def convert_html_to_pdf(html_content):
    # Convert the HTML content to PDF
    HTML(string=html_content).write_pdf(OUTPUT_PDF)
    print(f"PDF report saved to {OUTPUT_PDF}")


def main():
    # Load data
    news_data, stock_data = load_data()

    # Generate HTML report
    html_content = generate_html_report(news_data, stock_data)

    # Convert HTML to PDF
    # convert_html_to_pdf(html_content)


if __name__ == '__main__':
    main()
