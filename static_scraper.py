from bs4 import BeautifulSoup
import requests, time, random, csv


BASE = "http://quotes.toscrape.com/page/{page}/"


def get_page(page):
    """Fetch a page with get request, retrying on failures.
    
    Args:
        page (int): Page number to fetch.
    Returns:
        str|None: HTML content or None on failure.
    """
    for attempt in range(3):
        try:
            r = requests.get(BASE.format(page=page), timeout=10)
            r.raise_for_status() # for 4xx/5xx responses as exceptions
            return r.text # only the HTML content
        except Exception as e:
            print("Err: ", e)
            print("Retries: ", attempt + 1)
            time.sleep(5) 
    return None

def parse(html):
    """Parse HTML content with BeautifulSoup to extract the data (i.e., quotes).

    Args:
        html (str): HTML content of a page.
    Returns:
        list[dict]: List of quotes with text, author, and tags.
    """
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for q in soup.select(".quote"):
        rows.append({
            "text": q.select_one(".text").get_text(strip=True),
            "author": q.select_one(".author").get_text(strip=True),
            "tags": "|".join([t.get_text(strip=True) for t in q.select(".tags .tag")]) # for better display
        })
    return rows

def main():
    page = 1
    allrows = []
    # Loop through pages until no more data or an error occurs
    while True:
        html = get_page(page)
        if not html:
            break
        data = parse(html) # list of dicts with keys: "text", "author", "tags"
        if not data:
            break
        allrows.extend(data) # or allrows += data with slightly worse efficiency
        print("page", page, "->", len(data), "items")
        page += 1
        time.sleep(random.uniform(0.5, 1.5))
    with open("quotes.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
        writer.writeheader() # write column names (i.e., "text", "author", "tags")
        writer.writerows(allrows)
    print("Saved", len(allrows), "rows.")


if __name__ == "__main__":
    main()