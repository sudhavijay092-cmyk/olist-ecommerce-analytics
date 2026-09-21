import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

PROJECT_PATH = Path(r"D:\swiftcart-margin-under-pressure")

ANALYSIS_DATA_PATH = (
    PROJECT_PATH
    / "Data"
    / "cleaned"
    / "swiftcart_order_analysis.csv"
)

OUTPUT_PATH = PROJECT_PATH / "output" / "python"

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 2. LOAD ORDER-LEVEL ANALYSIS DATASET
# ============================================================

order_analysis = pd.read_csv(
    ANALYSIS_DATA_PATH
)


# ============================================================
# 3. CREATE VALID FREIGHT ANALYSIS DATASET
# ============================================================

freight_analysis = order_analysis[
    (order_analysis["total_product_value"].notna())
    & (order_analysis["total_freight_value"].notna())
    & (order_analysis["total_product_value"] > 0)
].copy()


# ============================================================
# 4. OVERALL FREIGHT ANALYSIS
# ============================================================

total_product_value = (
    freight_analysis["total_product_value"].sum()
)

total_freight_value = (
    freight_analysis["total_freight_value"].sum()
)

overall_freight_percentage = (
    total_freight_value
    / total_product_value
) * 100


print("\nSWIFTCART — FREIGHT AND MARGIN PRESSURE ANALYSIS")
print("=" * 65)

print("\n1. OVERALL FREIGHT BURDEN")
print("-" * 65)

print(
    f"Orders analyzed: {len(freight_analysis):,}"
)

print(
    f"Total product value: {total_product_value:,.2f}"
)

print(
    f"Total freight value: {total_freight_value:,.2f}"
)

print(
    f"Overall freight percentage: "
    f"{overall_freight_percentage:.2f}%"
)


# ============================================================
# 5. FREIGHT PERCENTAGE SUMMARY
# ============================================================

print("\n2. FREIGHT PERCENTAGE DISTRIBUTION")
print("-" * 65)

freight_summary = (
    freight_analysis["freight_percentage"]
    .describe(
        percentiles=[
            0.25,
            0.50,
            0.75,
            0.90,
            0.95
        ]
    )
)

print(
    freight_summary.round(2)
)


# ============================================================
# 6. HIGH FREIGHT BURDEN ORDERS
# ============================================================

orders_above_100 = freight_analysis[
    freight_analysis["freight_percentage"] > 100
]

print("\n3. EXTREME FREIGHT BURDEN")
print("-" * 65)

print(
    "Orders where freight exceeds "
    f"product value: {len(orders_above_100):,}"
)

print(
    "Percentage of analyzed orders: "
    f"{(len(orders_above_100) / len(freight_analysis)) * 100:.2f}%"
)


# ============================================================
# 7. PRODUCT VALUE GROUPS
# ============================================================

value_bins = [
    0,
    50,
    100,
    250,
    500,
    float("inf")
]

value_labels = [
    "Up to 50",
    "51–100",
    "101–250",
    "251–500",
    "500+"
]

freight_analysis["product_value_group"] = pd.cut(
    freight_analysis["total_product_value"],
    bins=value_bins,
    labels=value_labels,
    include_lowest=True
)


value_group_summary = (
    freight_analysis
    .groupby(
        "product_value_group",
        observed=False
    )
    .agg(
        orders=(
            "order_id",
            "count"
        ),
        average_product_value=(
            "total_product_value",
            "mean"
        ),
        average_freight_value=(
            "total_freight_value",
            "mean"
        ),
        average_freight_percentage=(
            "freight_percentage",
            "mean"
        )
    )
    .reset_index()
)


print("\n4. FREIGHT BURDEN BY PRODUCT VALUE GROUP")
print("-" * 65)

print(
    value_group_summary.round(2)
)


# ============================================================
# 8. CHART 1 — AVERAGE FREIGHT BURDEN
# ============================================================

plt.figure(
    figsize=(9, 5)
)

plt.bar(
    value_group_summary[
        "product_value_group"
    ].astype(str),
    value_group_summary[
        "average_freight_percentage"
    ]
)

plt.title(
    "Average Freight Burden by Product Value Group"
)

plt.xlabel(
    "Product Value Group"
)

plt.ylabel(
    "Average Freight Percentage"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH
    / "03_freight_burden_by_product_value_group.png",
    dpi=300
)

plt.close()


# ============================================================
# 9. CHART 2 — PRODUCT VALUE VS FREIGHT
# ============================================================

plt.figure(
    figsize=(9, 6)
)

scatter_data = freight_analysis[
    [
        "total_product_value",
        "total_freight_value"
    ]
].dropna()


plt.scatter(
    scatter_data[
        "total_product_value"
    ],
    scatter_data[
        "total_freight_value"
    ],
    alpha=0.3
)

plt.title(
    "Product Value vs Freight Cost"
)

plt.xlabel(
    "Total Product Value"
)

plt.ylabel(
    "Total Freight Value"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH
    / "04_product_value_vs_freight_cost.png",
    dpi=300
)

plt.close()


# ============================================================
# 10. KEY PYTHON FINDINGS
# ============================================================

highest_burden_group = (
    value_group_summary.loc[
        value_group_summary[
            "average_freight_percentage"
        ].idxmax()
    ]
)

lowest_burden_group = (
    value_group_summary.loc[
        value_group_summary[
            "average_freight_percentage"
        ].idxmin()
    ]
)


print("\n5. KEY PYTHON FINDINGS")
print("-" * 65)

print(
    f"Overall freight burden: "
    f"{overall_freight_percentage:.2f}%"
)

print(
    f"Highest average freight burden group: "
    f"{highest_burden_group['product_value_group']} "
    f"({highest_burden_group['average_freight_percentage']:.2f}%)"
)

print(
    f"Lowest average freight burden group: "
    f"{lowest_burden_group['product_value_group']} "
    f"({lowest_burden_group['average_freight_percentage']:.2f}%)"
)

print(
    "\nPython freight and margin pressure analysis completed."
)

print(
    f"Charts saved to: {OUTPUT_PATH}"
)