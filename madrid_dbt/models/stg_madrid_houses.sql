with source as (

    select * from read_csv_auto('C:/Users/samue/OneDrive/Skrivbord/Madrid_Real_Estate/data_raw/houses_Madrid_cleaned.csv')

),

staged as (

    select
        id,
        sq_mt_built,
        sq_mt_useful,
        n_rooms,
        n_bathrooms,
        neighborhood_id,
        buy_price,
        buy_price_by_area,
        rent_price,
        rent_price_by_area,
        house_type_id,
        is_renewal_needed,
        is_new_development,
        built_year,
        has_ac,
        has_lift,
        has_pool,
        has_terrace,
        has_balcony,
        has_parking,
        is_exterior,
        has_garden,
        latitude,
        longitude
    from source

)

select * from staged