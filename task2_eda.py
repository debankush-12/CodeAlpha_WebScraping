import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("books_dataset.csv")

print("=" * 60)
print("BOOKS DATASET - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Columns:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Titles:")
print(df["Title"].duplicated().sum())

df = df.drop_duplicates(subset=["Title"])

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
df["Rating"] = df["Rating"].astype(str).str.strip()
df["Availability"] = df["Availability"].astype(str).str.strip()

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Number"] = df["Rating"].map(rating_map)

print("\n" + "=" * 60)
print("STATISTICAL SUMMARY")
print("=" * 60)

print(df["Price"].describe())

print("\nMinimum Price:")
print(df["Price"].min())

print("\nMaximum Price:")
print(df["Price"].max())

print("\nAverage Price:")
print(df["Price"].mean())

print("\nMedian Price:")
print(df["Price"].median())

print("\nStandard Deviation:")
print(df["Price"].std())

print("\nPrice Range:")
print(df["Price"].max() - df["Price"].min())

cheapest_book = df.loc[df["Price"].idxmin()]

print("\n" + "=" * 60)
print("CHEAPEST BOOK")
print("=" * 60)
print(cheapest_book)

most_expensive_book = df.loc[df["Price"].idxmax()]

print("\n" + "=" * 60)
print("MOST EXPENSIVE BOOK")
print("=" * 60)
print(most_expensive_book)

print("\n" + "=" * 60)
print("RATING DISTRIBUTION")
print("=" * 60)

print(df["Rating"].value_counts())

rating_percentage = (
    df["Rating"]
    .value_counts(normalize=True)
    * 100
)

print("\nRating Percentage:")
print(rating_percentage)

print("\nAverage Rating:")
print(df["Rating_Number"].mean())

print("\n" + "=" * 60)
print("FIVE STAR BOOKS")
print("=" * 60)

highest_rated = df[
    df["Rating_Number"] == 5
]

print(
    highest_rated[
        ["Title", "Price", "Rating"]
    ].head(10)
)

rating_price = df.groupby(
    "Rating"
)["Price"].mean().sort_values(
    ascending=False
)

print("\n" + "=" * 60)
print("AVERAGE PRICE BY RATING")
print("=" * 60)

print(rating_price)

correlation = df[
    ["Price", "Rating_Number"]
].corr()

print("\n" + "=" * 60)
print("PRICE-RATING CORRELATION")
print("=" * 60)

print(correlation)

plt.figure(figsize=(10, 6))

plt.hist(
    df["Price"],
    bins=30
)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig(
    "price_distribution.png",
    dpi=300
)

plt.show()

plt.figure(figsize=(8, 5))

rating_counts = df["Rating"].value_counts()

sns.barplot(
    x=rating_counts.index,
    y=rating_counts.values
)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig(
    "rating_distribution.png",
    dpi=300
)

plt.show()

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Rating_Number",
    y="Price"
)

plt.title("Book Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")

plt.tight_layout()
plt.savefig(
    "price_vs_rating.png",
    dpi=300
)

plt.show()

plt.figure(figsize=(8, 5))

sns.boxplot(
    y=df["Price"]
)

plt.title("Book Price Distribution")
plt.ylabel("Price (£)")

plt.tight_layout()
plt.savefig(
    "price_boxplot.png",
    dpi=300
)

plt.show()

df.to_csv(
    "books_cleaned.csv",
    index=False,
    encoding="utf-8"
)

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY!")
print("=" * 60)

print("Total Books:", len(df))
print("Total Columns:", len(df.columns))
print("Cleaned Dataset: books_cleaned.csv")
print("Charts Saved:")
print("price_distribution.png")
print("rating_distribution.png")
print("price_vs_rating.png")
print("price_boxplot.png")
print("=" * 60)