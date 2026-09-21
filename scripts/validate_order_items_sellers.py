import pandas as pd

order_items = pd.read_csv(
    "data/raw_public/olist_order_items_dataset.csv",
    usecols=["seller_id"]
)

sellers = pd.read_csv(
    "data/raw_public/olist_sellers_dataset.csv",
    usecols=["seller_id"]
)

print("=" * 60)
print("ORDER ITEMS → SELLERS REFERENTIAL INTEGRITY")
print("=" * 60)

print("\nOrder item rows:", len(order_items))
print("Unique seller IDs in order items:",
      order_items["seller_id"].nunique())

print("Sellers:", len(sellers))
print("Unique seller IDs in sellers:",
      sellers["seller_id"].nunique())

missing_sellers = order_items.loc[
    ~order_items["seller_id"].isin(sellers["seller_id"])
]

print("\nOrder item rows with missing seller reference:",
      len(missing_sellers))

print("Unique missing seller IDs:",
      missing_sellers["seller_id"].nunique())