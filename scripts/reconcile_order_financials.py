import pandas as pd

orders = pd.read_csv(
    "data/raw_public/olist_orders_dataset.csv",
    usecols=["order_id", "order_status"]
)

items = pd.read_csv(
    "data/raw_public/olist_order_items_dataset.csv",
    usecols=["order_id", "price", "freight_value"]
)

payments = pd.read_csv(
    "data/raw_public/olist_order_payments_dataset.csv",
    usecols=["order_id", "payment_value"]
)

# Aggregate item-level values to order level
item_summary = (
    items
    .groupby("order_id", as_index=False)
    .agg(
        item_value=("price", "sum"),
        freight_value=("freight_value", "sum")
    )
)

# Aggregate payment values to order level
payment_summary = (
    payments
    .groupby("order_id", as_index=False)
    .agg(
        payment_value=("payment_value", "sum")
    )
)

# Combine
reconciliation = (
    orders
    .merge(item_summary, on="order_id", how="left")
    .merge(payment_summary, on="order_id", how="left")
)

reconciliation["item_plus_freight"] = (
    reconciliation["item_value"].fillna(0)
    + reconciliation["freight_value"].fillna(0)
)

reconciliation["payment_value"] = (
    reconciliation["payment_value"].fillna(0)
)

reconciliation["difference"] = (
    reconciliation["payment_value"]
    - reconciliation["item_plus_freight"]
)

print("=" * 60)
print("ORDER-LEVEL FINANCIAL RECONCILIATION")
print("=" * 60)

print("\n1. Orders:")
print(len(reconciliation))

print("\n2. Orders with item data:")
print(reconciliation["item_value"].notna().sum())

print("\n3. Orders with payment data:")
print(reconciliation["payment_value"].ne(0).sum())

print("\n4. Difference summary:")
print(reconciliation["difference"].describe())

print("\n5. Orders where payment differs from item + freight:")
print(
    (reconciliation["difference"].abs() > 0.01).sum()
)

print("\n6. Orders where payment is lower than item + freight:")
print(
    (
        reconciliation["payment_value"]
        < reconciliation["item_plus_freight"] - 0.01
    ).sum()
)

print("\n7. Orders where payment is higher than item + freight:")
print(
    (
        reconciliation["payment_value"]
        > reconciliation["item_plus_freight"] + 0.01
    ).sum()
)

print("\n8. Example largest absolute differences:")

print(
    reconciliation[
        [
            "order_id",
            "order_status",
            "item_value",
            "freight_value",
            "payment_value",
            "difference"
        ]
    ]
    .assign(
        abs_difference=lambda x: x["difference"].abs()
    )
    .sort_values("abs_difference", ascending=False)
    .head(10)
    .to_string(index=False)
)