from bs4 import BeautifulSoup
import requests, time, sqlite3, hashlib


BASE = "http://quotes.toscrape.com/page/{page}/"
DB = "./data/quotes.db"


def ensure_db():
    """To ensure the sqlite3 database and the quotes table exist."""
    con = sqlite3.connect(DB)
    c = con.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY,
        text TEXT,
        author TEXT,
        tags TEXT,
        text_hash TEXT UNIQUE,
        source TEXT
    )
    """)
    con.commit()
    con.close()

def text_hash(s):
    """Generate a SHA-256 hash for a given string (for deduplication).

    Args:
        s (str): Input string.
    Returns:
        str: 32-Byte hexadecimal representation from the SHA-256 hashing.
    """
    return hashlib.sha256(s.encode("utf-8")).hexdigest() # the `encode` method converts str to bytes

def get_page(page):
    """Fetch a page with get request, retrying on failures.
    
    Args:
        page (int): Page number to fetch.
    Returns:
        str | None: HTML content or None on failure.
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

def save_row(row):
    """Save a single quote row to the database, while relying on the uniqueness constraint to avoid duplicates.

    Args:
        row (dict): A dictionary with keys: "text", "author", "tags", and optionally "source".
    Returns:
        None    
    """
    con = sqlite3.connect(DB)
    c = con.cursor()
    try:
        c.execute("INSERT INTO quotes (text, author, tags, text_hash, source) VALUES (?, ?, ?, ?, ?)",
                  (row['text'], row['author'], row['tags'], text_hash(row['text']), row.get('source','quotes.toscrape')))
        con.commit()
    except sqlite3.IntegrityError:
        # if the quote already exists (based on the uniqueness constraint check on `text_hash`)
        pass
    finally:
        con.close()

def check_db():
    """Print a few sample rows from the database for verification."""
    con = sqlite3.connect(DB)
    c = con.cursor()
    for row in c.execute("SELECT id, text, author, tags, source FROM quotes LIMIT 10"):
        print(row)
    con.close()

def main():
    ensure_db()
    page = 1
    # Loop through pages until no more data or an error occurs
    while True:
        html = get_page(page)
        if not html:
            break
        data = parse(html) # list of dicts with keys: "text", "author", "tags"
        if not data:
            break
        for row in data:
            save_row(row)
        print(f"Saved rows in page {page}: {len(data)}")
        page += 1
        time.sleep(1)
    print("\nSample data from the database:")
    check_db()


if __name__ == "__main__":
    main()