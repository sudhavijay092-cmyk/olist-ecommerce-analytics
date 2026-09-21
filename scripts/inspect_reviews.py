import pandas as pd

file_path = "data/raw_public/olist_order_reviews_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("ORDER REVIEWS TABLE — BASIC PROFILE")
print("=" * 60)

print("\n1. Shape:")
print(df.shape)

print("\n2. Column names:")
print(df.columns.tolist())

print("\n3. Data types:")
print(df.dtypes)

print("\n4. Missing values:")
print(df.isna().sum())

print("\n5. First 5 rows:")
print(df.head())

print("\n6. Unique order IDs:")
print(df["order_id"].nunique())

print("\n7. Unique review IDs:")
print(df["review_id"].nunique())

print("\n8. Review score distribution:")
print(df["review_score"].value_counts().sort_index())

print("\n9. Review creation date range:")
print(
    df["review_creation_date"].min(),
    "to",
    df["review_creation_date"].max()
)