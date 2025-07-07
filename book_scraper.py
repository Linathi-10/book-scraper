# book_scraper.py
# Scrapes all books from https://books.toscrape.com and saves them to books_all_pages.csv

import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# Starting point of the site
base_url = "https://books.toscrape.com/"
url = base_url + "catalogue/page-1.html"

# This will store all scraped book data
all_books = []

# Loop through each page until no 'Next' button is found
while url:
    print(f"Scraping: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]
        link = urljoin(base_url, book.h3.a["href"])

        all_books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Link": link
        })

    # Move to the next page
    next_btn = soup.find("li", class_="next")
    if next_btn:
        next_page = next_btn.a["href"]
        url = urljoin(url, next_page)
    else:
        url = None  # No more pages

# Save data to CSV
df = pd.DataFrame(all_books)
df.to_csv("books_all_pages.csv", index=False)

print("✅ Done! All books scraped and saved to 'books_all_pages.csv'")
