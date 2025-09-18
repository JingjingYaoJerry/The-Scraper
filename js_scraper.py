from playwright.sync_api import sync_playwright
import csv

# As demonstrated in Playwright's official docs (https://playwright.dev/python/docs/library)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True) # in a headless environment (i.e., without a visible UI)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/js/")
    page.wait_for_selector(".quote") # 
    quotes = page.query_selector_all(".quote")
    rows = []
    for q in quotes:
        rows.append({
            "text": q.query_selector(".text").inner_text(),
            "author": q.query_selector(".author").inner_text(),
            "tags": "|".join([t.inner_text() for t in q.query_selector_all(".tags .tag")])
        })
    with open("quotes_js.csv","w",newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["text","author","tags"])
        writer.writeheader()
        writer.writerows(rows)
    browser.close()