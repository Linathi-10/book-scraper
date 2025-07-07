# Book Scraper – Python Web Scraping Project

This script scrapes all book listings from [Books to Scrape](https://books.toscrape.com), a demo e-commerce site for practicing web scraping.

It collects the following details:
-  Book Title
-  Price
-  Rating
- Link to book detail page

All data is saved to a `.csv` file you can open in Excel.

---

## 🔧 Tools & Libraries

- `requests` – fetches web pages
- `BeautifulSoup` – parses HTML
- `pandas` – stores and saves data to CSV
- `urllib.parse` – handles clean URL links

---

##  How It Works

1. Visits the first catalog page
2. Finds all books on the page using class selectors
3. Follows the “Next” button to paginate through all 50 pages
4. Stores each book’s title, price, rating, and link
5. Exports everything to `books_all_pages.csv`

---

## 🧪 Sample Output (CSV)

| Title                      | Price   | Rating | Link                                  |
|----------------------------|---------|--------|---------------------------------------|
| A Light in the Attic       | £51.77  | Three  | https://books.toscrape.com/...        |
| Tipping the Velvet         | £53.74  | One    | https://books.toscrape.com/...        |
| Soumission                 | £50.10  | One    | https://books.toscrape.com/...        |

---

## 📂 How to Run

```bash
python book_scraper.py

Requires:

Python 3.x

Libraries installed with pip install requests beautifulsoup4 pandas
books_all_pages.csv
 Built by Linathi Tywakadi | July 2025












