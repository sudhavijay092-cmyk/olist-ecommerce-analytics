import pandas as pd

products = pd.read_csv(
    "data/raw_public/olist_products_dataset.csv",
    usecols=["product_category_name"]
)

translation = pd.read_csv(
    "data/raw_public/product_category_name_translation.csv",
    usecols=["product_category_name"]
)

product_categories = set(
    products["product_category_name"]
    .dropna()
    .unique()
)

translated_categories = set(
    translation["product_category_name"]
    .dropna()
    .unique()
)

missing_translations = sorted(
    product_categories - translated_categories
)

print("=" * 60)
print("PRODUCTS → CATEGORY TRANSLATION VALIDATION")
print("=" * 60)

print("\nUnique product categories:",
      len(product_categories))

print("Unique translated categories:",
      len(translated_categories))

print("\nProduct categories without translation:",
      len(missing_translations))

print("\nMissing translation categories:")
for category in missing_translations:
    print(category)