import pandas as pd

file_path = "data/raw_public/olist_order_items_dataset.csv"

df = pd.read_csv(
    file_path,
    usecols=["order_id", "order_item_id"]
)

print("=" * 60)
print("ORDER ITEMS COMPOSITE KEY VALIDATION")
print("=" * 60)

print("\n1. Total rows:")
print(len(df))

print("\n2. Unique (order_id, order_item_id) combinations:")
print(
    df.drop_duplicates(
        subset=["order_id", "order_item_id"]
    ).shape[0]
)

print("\n3. Duplicate (order_id, order_item_id) combinations:")

duplicates = df.duplicated(
    subset=["order_id", "order_item_id"],
    keep=False
)

print(duplicates.sum())

print("\n4. Number of duplicated key combinations:")
print(
    df.loc[duplicates, ["order_id", "order_item_id"]]
    .drop_duplicates()
    .shape[0]
)

print("\n5. Example duplicated combinations:")

print(
    df.loc[
        duplicates,
        ["order_id", "order_item_id"]
    ]
    .sort_values(["order_id", "order_item_id"])
    .head(20)
    .to_string(index=False)
)