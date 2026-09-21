import pandas as pd

file_path = "data/raw_public/olist_order_reviews_dataset.csv"

df = pd.read_csv(file_path)

duplicate_ids = df[
    df["review_id"].duplicated(keep=False)
]

print("=" * 60)
print("REVIEW DUPLICATE CONTENT INVESTIGATION")
print("=" * 60)

columns_to_check = [
    "review_score",
    "review_comment_title",
    "review_comment_message",
    "review_creation_date",
    "review_answer_timestamp"
]

print("\n1. Duplicated review IDs:", duplicate_ids["review_id"].nunique())

print("\n2. Number of unique values per field among duplicated review IDs:")

summary = (
    duplicate_ids
    .groupby("review_id")[columns_to_check]
    .nunique()
)

print(summary.describe())

print("\n3. Review IDs where review score differs:")
score_variation = summary[summary["review_score"] > 1]
print("Count:", len(score_variation))

print("\n4. Review IDs where review comment differs:")
comment_variation = summary[
    (summary["review_comment_title"] > 1) |
    (summary["review_comment_message"] > 1)
]
print("Count:", len(comment_variation))

print("\n5. Example duplicated review IDs with full records:")

example_ids = duplicate_ids["review_id"].drop_duplicates().head(3)

print(
    duplicate_ids[
        duplicate_ids["review_id"].isin(example_ids)
    ][
        ["review_id", "order_id"] + columns_to_check
    ].to_string(index=False)
)