import pandas as pd

file_path = "data/raw_public/olist_orders_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("ORDERS TABLE — BASIC PROFILE")
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

print("\n6. Date range:")
print("Order purchase timestamp:",
      df["order_purchase_timestamp"].min(),
      "to",
      df["order_purchase_timestamp"].max())

print("Order delivered customer date:",
      df["order_delivered_customer_date"].min(),
      "to",
      df["order_delivered_customer_date"].max())

print("\n7. Order ID uniqueness:")
print("Total rows:", len(df))
print("Unique order IDs:", df["order_id"].nunique())
print("Duplicate order IDs:", df["order_id"].duplicated().sum())

print("\n8. Order status distribution:")
print(df["order_status"].value_counts())

print("\n9. Missing delivery dates by order status:")
print(
    df.groupby("order_status")[
        ["order_delivered_carrier_date", "order_delivered_customer_date"]
    ]
    .apply(lambda x: x.isna().sum())
)      