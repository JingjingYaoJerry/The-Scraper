# The Scraper - Demo for Scraping

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/Playwright-Enabled-green.svg)](https://playwright.dev/docs/intro)
[![Scrapy](https://img.shields.io/badge/Scrapy-Enabled-yellow.svg)](https://scrapy.org/)
[![Made-with-Love](https://img.shields.io/badge/Made%20with-❤️-ff69b4.svg)](https://www.linkedin.com/in/%E4%BA%AC%E6%99%B6-%E5%A7%9A-9997b5180/)

---

### Key Features

* **Static Scraping**: Scrape data from [quotes.toscrape.com](http://quotes.toscrape.com) across multiple pages.
* **JS-Rendered Scraping**: Scrape data from [quotes.toscrape.com](http://quotes.toscrape.com) with `Playwright`.
* **DB Storage**: Store scraped data with a `sqlite3` DB.
* **Scrapy Spider**: Scrape data with a `Scrapy` spider.
* **Basic Data Analysis**: Clean and analyze scraped data with `pandas` and `Matplotlib`.
* **CLI Entry Point**: Run demos with a simple CLI.

--- 

### Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/JingjingYaoJerry/The-Scraper.git
    ```

2.  **Install dependencies and browsers:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

3.  **Run modules directly for various scraping (and storage) methods:**
    ```bash
    python static_scraper.py
    python static_scraper_db.py
    scrapy runspider scrapy_scraper.py -o data/quotes.json
    python js_scraper.py
    python analysis.py
    ```

4.  **Or run via CLI:**
    ```bash
    python cli.py --mode static_csv
    python cli.py --mode static_db
    python cli.py --mode js
    python cli.py --mode static_scrapy
    ```

---

### Project Structure

* `requirements.txt`: A list of all necessary Python packages.
* `cli.py`: The interactive entry point through the command line.
* `static_scraper.py`: The module for scraping data across all pages in a static "request & parse" manner.
* `static_scraper_db.py`: The module for static scraping across all pages where the outputs are stored in a sqlite3 DB.
* `scrapy_scraper.py`: The module for static scraping with Scrapy.
* `js_scraper.py`: The module for scraping data from a JS-rendered website with Playwright
* `analysis.py`: The module for performing basic analysis to the scraped data.
* `./data/`: The directory for all outputs.

---

### Outputs

* `./data/quotes.csv`: Outputs in CSV from scraping http://quotes.toscrape.com.
* `./data/quotes.db`: Outputs in a sqlite3 DB from scraping http://quotes.toscrape.com.
* `./data/quotes.json`: Outputs in json from scraping http://quotes.toscrape.com with Scrapy.
* `./data/quotes_js.csv`: Outputs from scraping http://quotes.toscrape.com/js/.
* `./data/authors.png`: Visualization on authors' distribution from analyzing quotes.csv.
* `./data/tags.png`: Visualization on tags' distribution from analyzing quotes.csv.