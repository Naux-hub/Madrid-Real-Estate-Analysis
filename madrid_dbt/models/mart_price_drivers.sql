with houses as (

    select * from {{ ref('stg_madrid_houses') }}

),

analysis as (

    select
        round(avg(case when has_pool = true then buy_price end), 0) as avg_price_with_pool,
        round(avg(case when has_pool = false then buy_price end), 0) as avg_price_without_pool,
        round(avg(case when has_parking = true then buy_price end), 0) as avg_price_with_parking,
        round(avg(case when has_parking = false then buy_price end), 0) as avg_price_without_parking,
        round(avg(case when has_terrace = true then buy_price end), 0) as avg_price_with_terrace,
        round(avg(case when has_terrace = false then buy_price end), 0) as avg_price_without_terrace,
        round(avg(case when has_ac = true then buy_price end), 0) as avg_price_with_ac,
        round(avg(case when has_ac = false then buy_price end), 0) as avg_price_without_ac,
        round(avg(case when is_new_development = true then buy_price end), 0) as avg_price_new,
        round(avg(case when is_new_development = false then buy_price end), 0) as avg_price_old,
        round(avg(case when is_exterior = true then buy_price end), 0) as avg_price_exterior,
        round(avg(case when is_exterior = false then buy_price end), 0) as avg_price_interior
    from houses
    where buy_price > 0

)

select * from analysis