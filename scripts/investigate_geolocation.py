import pandas as pd

file_path = "data/raw_public/olist_geolocation_dataset.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("GEOLOCATION COORDINATE VALIDATION")
print("=" * 60)

invalid_lat = df[
    (df["geolocation_lat"] < -34) |
    (df["geolocation_lat"] > 6)
]

invalid_lng = df[
    (df["geolocation_lng"] < -74) |
    (df["geolocation_lng"] > -34)
]

print("\n1. Total geolocation rows:")
print(len(df))

print("\n2. Latitude outside expected Brazil range:")
print(len(invalid_lat))

print("\n3. Longitude outside expected Brazil range:")
print(len(invalid_lng))

print("\n4. Rows outside both latitude and longitude ranges:")

invalid_both = df[
    (df["geolocation_lat"] < -34) |
    (df["geolocation_lat"] > 6) |
    (df["geolocation_lng"] < -74) |
    (df["geolocation_lng"] > -34)
]

print(len(invalid_both))

print("\n5. Example suspicious records:")
print(
    invalid_both[
        [
            "geolocation_zip_code_prefix",
            "geolocation_lat",
            "geolocation_lng",
            "geolocation_city",
            "geolocation_state"
        ]
    ].head(20).to_string(index=False)
)