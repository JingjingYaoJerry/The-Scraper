from static_scraper import main as run_static_csv
from static_scraper_db import main as run_static_db
from js_scraper import main as run_js
from analysis import main as run_analysis
import argparse, subprocess, os


def main():
    # Ensure the ./data directory exists
    if not os.path.exists('./data'):
        os.makedirs('./data')

    p = argparse.ArgumentParser()
    p.add_argument('--mode', choices=['static_csv','static_db','js','static_scrapy'], default='js',
                   help="Choose from modes: 'static_csv' for static scraping with a CSV output, " \
                   "'static_db' for static scraping with Sqlite DB storage, " \
                   "'js' for JavaScript-rendered scraping with Playwright, "
                   "or 'static_scrapy' for (static) scraping using the Scrapy framework.")
    args = p.parse_args()
    if args.mode == 'static_csv':
        run_static_csv()
    elif args.mode == 'static_db':
        run_static_db()
    elif args.mode == 'js':
        run_js()
        if input("Run analysis on the JS-scraped data now? (y/n): ").strip().lower() == 'y':
            run_analysis()
    elif args.mode == 'static_scrapy':
        subprocess.run(['scrapy','runspider','scrapy_scraper.py','-o','./data/quotes.json'])


if __name__ == "__main__":
    main()