# The Scraper - Demo for Scraping

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/Playwright-Enabled-green.svg)](https://playwright.dev/docs/intro)
[![Made-with-Love](https://img.shields.io/badge/Made%20with-❤️-ff69b4.svg)](https://www.linkedin.com/in/%E4%BA%AC%E6%99%B6-%E5%A7%9A-9997b5180/)

---

### Key Features

* **Static Scraping**: Scrape quotes from [quotes.toscrape.com](http://quotes.toscrape.com) across multiple pages.
* **JS-Rendered Scraping**: Scrape quotes from [quotes.toscrape.com](http://quotes.toscrape.com) with `Playwright`.
* **Basic Data Analysis**: Clean and analyze scraped data with `pandas` and `Matplotlib`.

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

3.  **Run static_scraper.py to scrape http://quotes.toscrape.com (static):**
    ```bash
    python static_scraper.py
    ```

4.  **Run js_scraper.py to scrape http://quotes.toscrape.com/js/ (JS-Rendered):**
    ```bash
    python js_scraper.py
    ```

5.  **Run analysis.py to perform basic data analysis:**
    ```bash
    python analysis.py
    ```

---

### Project Structure

* `requirements.txt`: A list of all necessary Python packages.
* `static_scraper.py`: The module for scraping data across all pages in a static "request & parse" manner.
* `js_scraper.py`: The module for scraping data from a JS-rendered website with Playwright
* `analysis.py`: The module for performing basic analysis to the scraped data.

---

### Outputs

* `quotes.csv`: Outputs from scraping http://quotes.toscrape.com.
* `quotes_js.csv`: Outputs from scraping http://quotes.toscrape.com/js/.
* `authors.png`: Visualization on authors' distribution from analyzing quotes.csv.
* `tags.png`: Visualization on tags' distribution from analyzing quotes.csv.