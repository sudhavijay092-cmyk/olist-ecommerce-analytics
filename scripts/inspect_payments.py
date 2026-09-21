import pandas as pd

file_path = "data/raw_public/olist_order_payments_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("ORDER PAYMENTS TABLE — BASIC PROFILE")
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

print("\n7. Payment types:")
print(df["payment_type"].value_counts())

print("\n8. Payment installments:")
print(df["payment_installments"].value_counts().sort_index())

print("\n9. Payment value summary:")
print(df["payment_value"].describe())