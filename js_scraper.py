from playwright.sync_api import sync_playwright
import csv


BASE = "https://quotes.toscrape.com/js/"


def scrape_quotes():
    """Scrape quotes from the JS-rendered page using Playwright locators.
    
    Returns:
        list[dict]: List of quote data with keys: "text", "author", "tags".
    """
    # As demonstrated in Playwright's official docs (https://playwright.dev/python/docs/library)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # in a headless environment (i.e., without a visible UI)
        page = browser.new_page()
        page.goto(BASE)
        quotes = page.locator(".quote") # use Locator API as recommended in the docs
        count = quotes.count()
        print("Total quotes found:", count)

        rows = []
        # Iterate through each quote and extract
        for i in range(count):
            q = quotes.nth(i)
            text = q.locator(".text").inner_text()
            author = q.locator(".author").inner_text()
            tags = "|".join(q.locator(".tags .tag").all_inner_texts())
            rows.append({"text": text, "author": author, "tags": tags})

        browser.close()
        print(f"Scraped {len(rows)} quotes.")
        return rows

def save_to_csv(rows, filename="./data/quotes_js.csv"):
    """Save scraped rows to a CSV file.
    
    Args:
        rows (list[dict]): List of quote data.
    """
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, 
                                fieldnames=["text", "author", "tags"],
                                quoting=csv.QUOTE_ALL) # for handling semicolons that are misinterpreted as column separators
        writer.writeheader()
        writer.writerows(rows)

def main():
    rows = scrape_quotes()
    save_to_csv(rows)

if __name__ == "__main__":
    main()