import pandas as pd

customers = pd.read_csv(
    "data/raw_public/olist_customers_dataset.csv",
    usecols=["customer_zip_code_prefix"]
)

geo = pd.read_csv(
    "data/raw_public/olist_geolocation_dataset.csv",
    usecols=["geolocation_zip_code_prefix"]
)

customer_zips = set(
    customers["customer_zip_code_prefix"].unique()
)

geo_zips = set(
    geo["geolocation_zip_code_prefix"].unique()
)

missing_geo = sorted(customer_zips - geo_zips)

print("=" * 60)
print("CUSTOMERS → GEOLOCATION VALIDATION")
print("=" * 60)

print("\n1. Unique customer zip prefixes:")
print(len(customer_zips))

print("\n2. Unique geolocation zip prefixes:")
print(len(geo_zips))

print("\n3. Customer zip prefixes without geolocation:")
print(len(missing_geo))

print("\n4. Example missing customer zip prefixes:")
print(missing_geo[:20])

print("\n5. Customer rows whose zip prefix has no geolocation:")
print(
    customers[
        ~customers["customer_zip_code_prefix"].isin(geo_zips)
    ].shape[0]
)