import pandas as pd

file_path = "data/raw_public/product_category_name_translation.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("CATEGORY TRANSLATION TABLE — BASIC PROFILE")
print("=" * 60)

print("\n1. Shape:")
print(df.shape)

print("\n2. Column names:")
print(df.columns.tolist())

print("\n3. Data types:")
print(df.dtypes)

print("\n4. Missing values:")
print(df.isna().sum())

print("\n5. First 10 rows:")
print(df.head(10))

print("\n6. Unique Portuguese categories:")
print(df["product_category_name"].nunique())

print("\n7. Unique English categories:")
print(df["product_category_name_english"].nunique())

print("\n8. Duplicate Portuguese categories:")
print(df["product_category_name"].duplicated().sum())

print("\n9. Duplicate English categories:")
print(df["product_category_name_english"].duplicated().sum())