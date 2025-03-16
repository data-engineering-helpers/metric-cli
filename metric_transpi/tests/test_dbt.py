

import pytest
from metric_transpi.dbt import from_yaml, CalculationMethod, TimeGrains


def test_from_yaml_should_read_dbt_metrics_fileformat():
    # given
    example_yaml = "metric_transpi/tests/metrics__digital_analytics_simplified.yml"

    # when
    r = from_yaml(path=example_yaml)
    
    # then
    assert r[0].name == 'number_of_sessions'
    assert r[0].label == 'Number total of sessions'
    assert r[0].model == "ref('stg_tracking_ecom_events')"
    assert r[0].description == "The count of distinct sessions"
    assert r[0].calculation_method == CalculationMethod.COUNT_DISTINCT
    assert r[0].expression == 'session_id'
    assert r[0].timestamp == 'event_date'
    assert r[0].time_grains == [TimeGrains.DAY, TimeGrains.WEEK, TimeGrains.MONTH, TimeGrains.QUARTER, TimeGrains.YEAR]
    assert r[0].dimensions == ["name", "provider", "country_code"]

def test_from_yaml_should_iterate_to_return_all_metrics():
    # given
    example_yaml = "metric_transpi/tests/metrics__digital_analytics_simplified.yml"

    # when
    r = from_yaml(path=example_yaml)
    
    # then
    assert 2 == len(r)
    assert r[0].name == 'number_of_sessions'
    assert r[1].name == 'number_of_session_with_product_purchased'


def test_from_yaml_should_raise_exception_when_file_isnot_about_metric_or_badly_formatted():
    # given
    example_yaml = "metric_transpi/tests/bad_formatted_metric.yml"

    # when
    with pytest.raises(ValueError) as excinfo:
        _ = from_yaml(path=example_yaml)
    
    # then
    assert isinstance(excinfo.value, ValueError)

