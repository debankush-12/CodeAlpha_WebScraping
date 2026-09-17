import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import time

BASE_URL = "https://books.toscrape.com/"
data = []

print("=" * 60)
print("BOOKS TO SCRAPE - WEB SCRAPING PROJECT")
print("=" * 60)

for page in range(1, 51):
    url = urljoin(
        BASE_URL,
        f"catalogue/page-{page}.html"
    )

    print(f"Scraping Page {page}/50...")

    try:
        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        books = soup.find_all(
            "article",
            class_="product_pod"
        )

        for book in books:
            title = book.h3.a["title"].strip()

            price = book.find(
                "p",
                class_="price_color"
            ).text.strip()

            rating = book.find(
                "p",
                class_="star-rating"
            )["class"][1]

            availability = book.find(
                "p",
                class_="instock availability"
            ).text.strip()

            relative_url = book.h3.a["href"]

            product_url = urljoin(
                url,
                relative_url
            )

            data.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability,
                "Product_URL": product_url
            })

        time.sleep(0.5)

    except requests.exceptions.RequestException as e:
        print(f"Error scraping page {page}: {e}")

df = pd.DataFrame(data)

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

df["Title"] = df["Title"].astype(str).str.strip()

df["Availability"] = (
    df["Availability"]
    .astype(str)
    .str.strip()
)

df["Rating"] = (
    df["Rating"]
    .astype(str)
    .str.strip()
)

df.drop_duplicates(
    subset=["Title"],
    inplace=True
)

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("Total Books:", len(df))
print("Total Columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 10 Records:")
print(df.head(10).to_string(index=False))

df.to_csv(
    "books_dataset.csv",
    index=False,
    encoding="utf-8"
)

print("\n" + "=" * 60)
print("SCRAPING COMPLETED SUCCESSFULLY!")
print("=" * 60)
print("Total records saved:", len(df))
print("Dataset file: books_dataset.csv")
print("=" * 60)