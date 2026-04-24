with houses as (

    select * from {{ ref('stg_madrid_houses') }}

),

analysis as (

    select
        neighborhood_id,
        count(*) as total_listings,
        round(avg(buy_price), 0) as avg_price,
        round(min(buy_price), 0) as min_price,
        round(max(buy_price), 0) as max_price,
        round(avg(buy_price_by_area), 0) as avg_price_per_sqm,
        round(avg(sq_mt_built), 0) as avg_size_sqm,
        round(avg(n_rooms), 1) as avg_rooms
    from houses
    where buy_price > 0
    and neighborhood_id is not null
    group by neighborhood_id
    order by avg_price desc

)

select * from analysis