import pandas as pd

file_path = "data/raw_public/olist_products_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("PRODUCTS TABLE — BASIC PROFILE")
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

print("\n6. Product ID uniqueness:")
print("Total rows:", len(df))
print("Unique product_id:", df["product_id"].nunique())
print("Duplicate product_id:", df["product_id"].duplicated().sum())

print("\n7. Product category:")
print("Unique categories:", df["product_category_name"].nunique())
print(df["product_category_name"].value_counts().head(10))