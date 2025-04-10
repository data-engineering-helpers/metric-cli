select
    -- grain
    123 as transaction_id,
    '2025-01-01'::date as gmv_recorded_at_date,

    -- dimensions
    'FR' as economical_businessunit_country_code,
    'Trekking' as sport_univers_label,
    'instore' as transaction_touchpoint_name,
    'Salanche Mountain Store' as economical_businessunit_name,
    'direct' as seller_type

    --measures
    1 as gmv_amount_euros,
    1 as gmv_amount,