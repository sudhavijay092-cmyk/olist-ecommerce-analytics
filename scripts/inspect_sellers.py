import pandas as pd

file_path = "data/raw_public/olist_sellers_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("SELLERS TABLE — BASIC PROFILE")
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

print("\n6. Seller ID uniqueness:")
print("Total rows:", len(df))
print("Unique seller_id:", df["seller_id"].nunique())
print("Duplicate seller_id:", df["seller_id"].duplicated().sum())

print("\n7. Seller states:")
print("Unique states:", df["seller_state"].nunique())
print(df["seller_state"].value_counts().head(10))