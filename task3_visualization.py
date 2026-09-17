import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("books_cleaned.csv")

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Number"] = df["Rating"].map(rating_map)

plt.figure(figsize=(10, 6))

rating_counts = df["Rating"].value_counts()

sns.barplot(
    x=rating_counts.index,
    y=rating_counts.values
)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("01_rating_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 6))

plt.hist(
    df["Price"],
    bins=30
)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("02_price_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 6))

sns.boxplot(
    y=df["Price"]
)

plt.title("Book Price Distribution and Outliers")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.savefig("03_price_boxplot.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 6))

avg_price_rating = df.groupby(
    "Rating_Number"
)["Price"].mean()

sns.barplot(
    x=avg_price_rating.index,
    y=avg_price_rating.values
)

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.tight_layout()
plt.savefig("04_average_price_by_rating.png", dpi=300)
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
plt.savefig("05_price_vs_rating.png", dpi=300)
plt.show()

top_10 = df.nlargest(
    10,
    "Price"
).sort_values(
    "Price"
)

plt.figure(figsize=(10, 7))

plt.barh(
    top_10["Title"],
    top_10["Price"]
)

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.tight_layout()
plt.savefig("06_top_10_expensive_books.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 6))

correlation = df[
    ["Price", "Rating_Number"]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Price and Rating Correlation")
plt.tight_layout()
plt.savefig("07_correlation_heatmap.png", dpi=300)
plt.show()

print("=" * 60)
print("DATA VISUALIZATION COMPLETED SUCCESSFULLY!")
print("=" * 60)
print("Total Books:", len(df))
print("Total Visualizations: 7")
print("=" * 60)
print("Files Created:")
print("01_rating_distribution.png")
print("02_price_distribution.png")
print("03_price_boxplot.png")
print("04_average_price_by_rating.png")
print("05_price_vs_rating.png")
print("06_top_10_expensive_books.png")
print("07_correlation_heatmap.png")
print("=" * 60)