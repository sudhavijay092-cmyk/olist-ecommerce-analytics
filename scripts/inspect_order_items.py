import pandas as pd

file_path = "data/raw_public/olist_order_items_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("ORDER ITEMS TABLE — BASIC PROFILE")
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

print("\n7. Duplicate order IDs:")
print(df["order_id"].duplicated().sum())

print("\n8. Unique products:")
print(df["product_id"].nunique())

print("\n9. Unique sellers:")
print(df["seller_id"].nunique())

print("\n10. Order item number distribution:")
print(df["order_item_id"].value_counts().sort_index())