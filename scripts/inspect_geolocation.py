import pandas as pd

file_path = "data/raw_public/olist_geolocation_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("GEOLOCATION TABLE — BASIC PROFILE")
print("=" * 60)

print("\n1. Shape:")
print(df.shape)

print("\n2. Column names:")
print(df.columns.tolist())

print("\n3. Data types:")
print(df.dtypes)

print("\n4. Missing values:")
print(df.isna().sum())

print("\n5. First 5 rows:")
print(df.head())

print("\n6. Zip code prefix:")
print("Unique zip prefixes:", df["geolocation_zip_code_prefix"].nunique())

print("\n7. Cities:")
print("Unique cities:", df["geolocation_city"].nunique())

print("\n8. States:")
print("Unique states:", df["geolocation_state"].nunique())
print(df["geolocation_state"].value_counts().head(10))

print("\n9. Latitude summary:")
print(df["geolocation_lat"].describe())

print("\n10. Longitude summary:")
print(df["geolocation_lng"].describe())