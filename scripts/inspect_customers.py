import pandas as pd

file_path = "data/raw_public/olist_customers_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("CUSTOMERS TABLE — BASIC PROFILE")
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

print("\n6. Customer ID uniqueness:")
print("Total rows:", len(df))
print("Unique customer_id:", df["customer_id"].nunique())
print("Duplicate customer_id:", df["customer_id"].duplicated().sum())

print("\n7. Customer unique ID:")
print("Unique customer_unique_id:", df["customer_unique_id"].nunique())
print("Duplicate customer_unique_id:", df["customer_unique_id"].duplicated().sum())