import pandas as pd

order_items = pd.read_csv(
    "data/raw_public/olist_order_items_dataset.csv",
    usecols=["product_id"]
)

products = pd.read_csv(
    "data/raw_public/olist_products_dataset.csv",
    usecols=["product_id"]
)

print("=" * 60)
print("ORDER ITEMS → PRODUCTS REFERENTIAL INTEGRITY")
print("=" * 60)

print("\nOrder item rows:", len(order_items))
print("Unique product IDs in order items:",
      order_items["product_id"].nunique())

print("Products:", len(products))
print("Unique product IDs in products:",
      products["product_id"].nunique())

missing_products = order_items.loc[
    ~order_items["product_id"].isin(products["product_id"])
]

print("\nOrder item rows with missing product reference:",
      len(missing_products))

print("Unique missing product IDs:",
      missing_products["product_id"].nunique())