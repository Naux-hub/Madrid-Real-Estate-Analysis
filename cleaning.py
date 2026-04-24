import pandas as pd

print("1. EXTRACT: Läser in rådata...")
df = pd.read_csv('data_raw/houses_Madrid.csv')
print(f"   {len(df)} rader och {len(df.columns)} kolumner laddade.")

print("\n2. TRANSFORM: Städar datan...")

# Välj ut relevanta kolumner
df = df[[
    'id', 'sq_mt_built', 'sq_mt_useful', 'n_rooms', 'n_bathrooms',
    'neighborhood_id', 'operation', 'buy_price', 'buy_price_by_area',
    'is_buy_price_known', 'rent_price', 'rent_price_by_area',
    'is_rent_price_known', 'house_type_id', 'is_renewal_needed',
    'is_new_development', 'built_year', 'has_ac', 'has_lift',
    'has_pool', 'has_terrace', 'has_balcony', 'has_parking',
    'is_exterior', 'has_garden', 'latitude', 'longitude'
]]

# Ta bort rader utan pris
df_buy = df[df['is_buy_price_known'] == True].copy()
df_buy = df_buy[df_buy['buy_price'] > 0]

# Ta bort extremvärden (över 10 miljoner)
df_buy = df_buy[df_buy['buy_price'] < 10000000]

# Ta bort rader utan storlek
df_buy = df_buy[df_buy['sq_mt_built'] > 0]

# Fyll tomma värden
df_buy['n_rooms'] = df_buy['n_rooms'].fillna(0)
df_buy['n_bathrooms'] = df_buy['n_bathrooms'].fillna(0)
df_buy['built_year'] = df_buy['built_year'].fillna(0)

print(f"   {len(df_buy)} köpbostäder efter städning.")

print("\n3. LOAD: Sparar tvättad data...")
df_buy.to_csv('data_raw/houses_Madrid_cleaned.csv', index=False)
print("   Sparad som 'houses_Madrid_cleaned.csv'!")