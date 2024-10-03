

from metric_transpi.dbt import from_yaml
from metric_transpi.metric import CALCULATION_METHOD, TIME_GRAINS


def test_from_yaml():
    # given

    # when
    r1, r2 = from_yaml(path="metric_transpi/tests/metrics__digital_analytics_simplified.yml")
    
    # then
    assert r1.name == 'number_of_sessions'
    assert r1.label == 'Number total of sessions'
    assert r1.model == "stg_tracking_ecom_events"
    assert r1.description == "The count of distinct sessions"
    assert r1.calculation_method == CALCULATION_METHOD.count_distinct
    assert r1.expression == 'session_id'
    assert r1.timestamp == 'event_date'
    assert r1.time_grains == TIME_GRAINS.day
    assert r1.dimensions == ["name", "provider", "country_code"]
    
    assert r2.name == 'number_of_session_with_product_purchased'
    assert r2.label == 'Number of session with product purchased'
    assert r2.model == "stg_tracking_ecom_events"
    assert r2.description == "Number of session with product purchased"
    assert r2.calculation_method == CALCULATION_METHOD.count_distinct
    assert r2.expression == 'session_id'
    assert r2.timestamp == 'event_date'
    assert r2.time_grains == TIME_GRAINS.day
    assert r2.dimensions == ["event_date", "name", "provider", "country_code", "metadata.device_details.device_type"]