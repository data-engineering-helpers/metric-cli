

from metric_transpi.dbt import from_yaml
from metric_transpi.metric import CALCULATION_METHOD, TIME_GRAINS


def test_from_yaml():
    
    # given

    # when
    r = from_yaml(path="metric_transpi/tests/metrics__digital_analytics_simplified.yml")
    
    # then
    assert r.name == 'number_of_sessions'
    assert r.label == 'Number total of sessions'
    assert r.model == "stg_tracking_ecom_events"
    assert r.description == "The count of distinct sessions"
    assert r.calculation_method == CALCULATION_METHOD.count_distinct
    assert r.expression == 'session_id'
    assert r.timestamp == 'event_date'
    assert r.time_grains == TIME_GRAINS.day
    assert r.dimensions == ["name", "provider", "country_code"]
    

