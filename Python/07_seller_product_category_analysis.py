import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

PROJECT_PATH = Path(r"D:\swiftcart-margin-under-pressure")

CLEANED_DATA_PATH = (
    PROJECT_PATH
    / "Data"
    / "cleaned"
)

OUTPUT_PATH = (
    PROJECT_PATH
    / "output"
    / "python"
)

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 2. LOAD REQUIRED DATASETS
# ============================================================

order_items = pd.read_csv(
    CLEANED_DATA_PATH
    / "olist_order_items_clean.csv"
)

products = pd.read_csv(
    CLEANED_DATA_PATH
    / "olist_products_clean.csv"
)


# ============================================================
# 3. CREATE ITEM-LEVEL ANALYSIS DATASET
# ============================================================

item_analysis = order_items.merge(
    products[
        [
            "product_id",
            "product_category_name"
        ]
    ],
    on="product_id",
    how="left"
)


print("\nSWIFTCART — SELLER AND PRODUCT CATEGORY ANALYSIS")
print("=" * 70)

print(
    f"\nTotal order items analyzed: "
    f"{len(item_analysis):,}"
)

print(
    f"Missing product categories: "
    f"{item_analysis['product_category_name'].isna().sum():,}"
)


# ============================================================
# 4. PRODUCT CATEGORY PERFORMANCE
# ============================================================

category_summary = (
    item_analysis
    .groupby(
        "product_category_name",
        dropna=False,
        as_index=False
    )
    .agg(
        total_items=(
            "order_item_id",
            "count"
        ),
        total_product_value=(
            "price",
            "sum"
        ),
        total_freight_value=(
            "freight_value",
            "sum"
        )
    )
)


# Calculate freight burden
category_summary["freight_percentage"] = (
    category_summary["total_freight_value"]
    / category_summary["total_product_value"]
) * 100


# ============================================================
# 5. TOP PRODUCT CATEGORIES BY SALES VALUE
# ============================================================

top_categories_sales = (
    category_summary
    .sort_values(
        "total_product_value",
        ascending=False
    )
    .head(10)
)


print("\n1. TOP 10 PRODUCT CATEGORIES BY SALES VALUE")
print("-" * 70)

print(
    top_categories_sales[
        [
            "product_category_name",
            "total_items",
            "total_product_value",
            "freight_percentage"
        ]
    ]
    .round(2)
)


# ============================================================
# 6. PRODUCT CATEGORIES BY FREIGHT BURDEN
# ============================================================

# Remove very small categories so a few expensive
# shipments do not dominate the ranking.
meaningful_categories = category_summary[
    category_summary["total_items"] >= 100
].copy()


top_categories_freight = (
    meaningful_categories
    .sort_values(
        "freight_percentage",
        ascending=False
    )
    .head(10)
)


print("\n2. TOP 10 MEANINGFUL PRODUCT CATEGORIES BY FREIGHT BURDEN")
print("-" * 70)

print(
    top_categories_freight[
        [
            "product_category_name",
            "total_items",
            "total_product_value",
            "total_freight_value",
            "freight_percentage"
        ]
    ]
    .round(2)
)


# ============================================================
# 7. SELLER PERFORMANCE
# ============================================================

seller_summary = (
    item_analysis
    .groupby(
        "seller_id",
        as_index=False
    )
    .agg(
        total_items=(
            "order_item_id",
            "count"
        ),
        total_product_value=(
            "price",
            "sum"
        ),
        total_freight_value=(
            "freight_value",
            "sum"
        )
    )
)


seller_summary["freight_percentage"] = (
    seller_summary["total_freight_value"]
    / seller_summary["total_product_value"]
) * 100


# ============================================================
# 8. TOP SELLERS BY ITEM VOLUME
# ============================================================

top_sellers_volume = (
    seller_summary
    .sort_values(
        "total_items",
        ascending=False
    )
    .head(10)
)


print("\n3. TOP 10 SELLERS BY ORDER-ITEM VOLUME")
print("-" * 70)

print(
    top_sellers_volume.round(2)
)


# ============================================================
# 9. HIGH-VOLUME SELLERS WITH HIGH FREIGHT BURDEN
# ============================================================

# Use at least 100 items to avoid unreliable results
high_volume_sellers = seller_summary[
    seller_summary["total_items"] >= 100
].copy()


high_freight_sellers = (
    high_volume_sellers
    .sort_values(
        "freight_percentage",
        ascending=False
    )
    .head(10)
)


print("\n4. HIGH-VOLUME SELLERS WITH HIGHEST FREIGHT BURDEN")
print("-" * 70)

print(
    high_freight_sellers.round(2)
)


# ============================================================
# 10. CHART 1 — TOP PRODUCT CATEGORIES BY SALES VALUE
# ============================================================

chart_categories_sales = (
    top_categories_sales
    .sort_values(
        "total_product_value",
        ascending=True
    )
)


plt.figure(
    figsize=(10, 6)
)

plt.barh(
    chart_categories_sales[
        "product_category_name"
    ].astype(str),
    chart_categories_sales[
        "total_product_value"
    ]
)

plt.title(
    "Top 10 Product Categories by Sales Value"
)

plt.xlabel(
    "Total Product Value"
)

plt.ylabel(
    "Product Category"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH
    / "05_top_product_categories_by_sales.png",
    dpi=300
)

plt.close()


# ============================================================
# 11. CHART 2 — PRODUCT CATEGORIES BY FREIGHT BURDEN
# ============================================================

chart_categories_freight = (
    top_categories_freight
    .sort_values(
        "freight_percentage",
        ascending=True
    )
)


plt.figure(
    figsize=(10, 6)
)

plt.barh(
    chart_categories_freight[
        "product_category_name"
    ].astype(str),
    chart_categories_freight[
        "freight_percentage"
    ]
)

plt.title(
    "Product Categories with Highest Freight Burden"
)

plt.xlabel(
    "Freight Percentage"
)

plt.ylabel(
    "Product Category"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH
    / "06_product_categories_highest_freight_burden.png",
    dpi=300
)

plt.close()


# ============================================================
# 12. CHART 3 — TOP SELLERS BY ITEM VOLUME
# ============================================================

chart_sellers = (
    top_sellers_volume
    .sort_values(
        "total_items",
        ascending=True
    )
)


plt.figure(
    figsize=(10, 6)
)

plt.barh(
    chart_sellers[
        "seller_id"
    ].astype(str),
    chart_sellers[
        "total_items"
    ]
)

plt.title(
    "Top 10 Sellers by Order-Item Volume"
)

plt.xlabel(
    "Total Items"
)

plt.ylabel(
    "Seller ID"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH
    / "07_top_sellers_by_item_volume.png",
    dpi=300
)

plt.close()


# ============================================================
# 13. KEY FINDINGS
# ============================================================

highest_sales_category = (
    top_categories_sales
    .iloc[0]
)

highest_freight_category = (
    top_categories_freight
    .iloc[0]
)

highest_volume_seller = (
    top_sellers_volume
    .iloc[0]
)

highest_freight_seller = (
    high_freight_sellers
    .iloc[0]
)


print("\n5. KEY PYTHON FINDINGS")
print("-" * 70)

print(
    f"Highest sales category: "
    f"{highest_sales_category['product_category_name']} "
    f"({highest_sales_category['total_product_value']:.2f})"
)

print(
    f"Highest meaningful category freight burden: "
    f"{highest_freight_category['product_category_name']} "
    f"({highest_freight_category['freight_percentage']:.2f}%)"
)

print(
    f"Highest item-volume seller: "
    f"{highest_volume_seller['seller_id']} "
    f"({highest_volume_seller['total_items']:,} items)"
)

print(
    f"High-volume seller with highest freight burden: "
    f"{highest_freight_seller['seller_id']} "
    f"({highest_freight_seller['freight_percentage']:.2f}%)"
)


print(
    "\nPython seller and product category analysis completed."
)

print(
    f"Charts saved to: {OUTPUT_PATH}"
)