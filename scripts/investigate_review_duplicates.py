import pandas as pd

file_path = "data/raw_public/olist_order_reviews_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("REVIEW DUPLICATE INVESTIGATION")
print("=" * 60)

duplicate_reviews = df[
    df["review_id"].duplicated(keep=False)
].sort_values("review_id")

print("\n1. Rows belonging to duplicated review IDs:")
print(len(duplicate_reviews))

print("\n2. Number of duplicated review IDs:")
print(duplicate_reviews["review_id"].nunique())

print("\n3. Unique orders per duplicated review ID:")
orders_per_review = (
    duplicate_reviews
    .groupby("review_id")["order_id"]
    .nunique()
)

print(orders_per_review.value_counts().sort_index())

print("\n4. Review IDs linked to multiple orders:")
multi_order_reviews = orders_per_review[orders_per_review > 1]

print("Count:", len(multi_order_reviews))

print("\n5. Example duplicated review records:")
print(
    duplicate_reviews[
        ["review_id", "order_id"]
    ].head(20).to_string(index=False)
)