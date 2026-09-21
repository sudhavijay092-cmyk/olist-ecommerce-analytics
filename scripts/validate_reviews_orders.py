import pandas as pd

reviews = pd.read_csv(
    "data/raw_public/olist_order_reviews_dataset.csv",
    usecols=["review_id", "order_id"]
)

orders = pd.read_csv(
    "data/raw_public/olist_orders_dataset.csv",
    usecols=["order_id"]
)

print("=" * 60)
print("REVIEWS → ORDERS REFERENTIAL INTEGRITY")
print("=" * 60)

print("\nReview rows:", len(reviews))
print("Unique review IDs:", reviews["review_id"].nunique())
print("Unique order IDs in reviews:",
      reviews["order_id"].nunique())

print("Orders:", len(orders))
print("Unique order IDs in orders:",
      orders["order_id"].nunique())

missing_orders = reviews.loc[
    ~reviews["order_id"].isin(orders["order_id"])
]

print("\nReview rows with missing order reference:",
      len(missing_orders))

print("Unique missing order IDs:",
      missing_orders["order_id"].nunique())

print("\nDuplicate review IDs:",
      reviews["review_id"].duplicated().sum())

print("\nDuplicate order IDs in reviews:",
      reviews["order_id"].duplicated().sum())
