import pandas as pd

sellers = pd.read_csv(
    "data/raw_public/olist_sellers_dataset.csv",
    usecols=["seller_zip_code_prefix"]
)

geo = pd.read_csv(
    "data/raw_public/olist_geolocation_dataset.csv",
    usecols=["geolocation_zip_code_prefix"]
)

seller_zips = set(
    sellers["seller_zip_code_prefix"].unique()
)

geo_zips = set(
    geo["geolocation_zip_code_prefix"].unique()
)

missing_geo = sorted(seller_zips - geo_zips)

print("=" * 60)
print("SELLERS → GEOLOCATION VALIDATION")
print("=" * 60)

print("\n1. Unique seller zip prefixes:")
print(len(seller_zips))

print("\n2. Unique geolocation zip prefixes:")
print(len(geo_zips))

print("\n3. Seller zip prefixes without geolocation:")
print(len(missing_geo))

print("\n4. Example missing seller zip prefixes:")
print(missing_geo[:20])

print("\n5. Seller rows whose zip prefix has no geolocation:")
print(
    sellers[
        ~sellers["seller_zip_code_prefix"].isin(geo_zips)
    ].shape[0]
)
