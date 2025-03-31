
from metric_transpi.dbt import CalculationMethod, Metric, TimeGrains
from metric_transpi.translate import to_pulse


def test_to_pulse():
    # Given
    metric = Metric(
        name='total_turnover',
        model='sales_table',
        label='Turnover',
        description='the sum of turnover on sales',
        datasource_id='id_pulse_of_the_table_source',
        expression='amount',
        calculation_method=CalculationMethod.SUM,
        timestamp='date_transation',
        dimensions=[
                'business_unit',
                'country',
                'brand_name'
        ],
        time_grains=[
                TimeGrains.DAY,
                TimeGrains.WEEK
        ]
    )

    # When
    result = to_pulse(metric)

    # Then
    assert result.to_dict() == {
        'metadata': {
            'name': 'total_turnover', 
            'description': 'the sum of turnover on sales'
        },
        'specification': {
            'datasource': {
                'id': 'id_pulse_of_the_table_source'
            }, 
            'basic_specification': {
                'measure': {
                    'field': 'amount',
                    'aggregation': 'AGGREGATION_SUM'
                }, 
                'time_dimension':{
                    'field': 'date_transation'
                }
            }, 
            'is_running_total': True
        },
        'extension_options': {
            'allowed_dimensions': [
                'business_unit',
                'country',
                'brand_name'
            ],
            'allowed_granularities': [
                'GRANULARITY_BY_DAY',
                'GRANULARITY_BY_WEEK'
            ]
        },
        'representation_options': {},
        'insights_options': {},
        "comparisons": {
                "comparisons": [
                    {
                        "compare_config": {
                            "comparison": "TIME_COMPARISON_PREVIOUS_PERIOD"
                        }
                    }
                ]
            }
    }
