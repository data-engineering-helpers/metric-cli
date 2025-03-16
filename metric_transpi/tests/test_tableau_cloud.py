
import requests
import json
from unittest.mock import MagicMock, call, patch
from metric_transpi.dbt import CalculationMethod, Metric, TimeGrains
from metric_transpi.tableau_cloud import from_metric_to_metricdef, list_metric, signin

@patch("requests.api")
def test_sigin(mock_requests):
    # Given
    host = "tableau-api-host.toto"
    pat_name = "papat"
    pat_secret = "password"
    site_url_id = "tableau"
    response = MagicMock()
    response.content = json.dumps(
        { 
            "credentials": { "site": {
                "id": "site_id_OK",
                "contentUrl": "site_url_OK"
                },
                "token": "OK"
            }
    })
    requests.api.post = MagicMock(return_value=response)

    
    # When
    token, site_id = signin(
        host=host, 
        site_url_id=site_url_id,
        pat_token_name=pat_name, 
        pat_token_secret=pat_secret
    )

    # Then
    assert requests.api.post.call_args == call(
        'https://tableau-api-host.toto/api/3.24/auth/signin', 
        headers={'accept': 'application/json', 'content-type': 'application/json'}, 
        json={'credentials': {'personalAccessTokenName': 'papat', 'personalAccessTokenSecret': 'password', 'site': {'contentUrl': 'tableau'}}})
    assert token == "OK"
    assert site_id == "site_id_OK"

@patch("openapi_client.api.metric_definitions_api.MetricDefinitionsApi.metric_query_service_list_definitions")
def test_list_metric(mock_openapi):
    # Given
    host = "tableau-api-host.toto"
    fake_token = "fake"
    response = mock_openapi.return_value
    response.to_json.return_value = {"definitions": [ {"metadata": {} } ]}
    
    # When
    json_result = list_metric(
        host=host, 
        api_token=fake_token
    )

    # Then
    assert mock_openapi.call_args == call(x_tableau_auth=fake_token, enable_sorting=True)
    assert json_result == json.loads('{"definitions": [ {"metadata": {} } ]}')


# def test_create_metric():
#     # Given
    
#     # When
#     json_result = create_metric(host='', api_token='')

#     # Then
#     assert json_result == {}


def test_from_metric_to_metricdef():
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
    result = from_metric_to_metricdef(metric)

    # Then
    assert result.to_dict() == {
        'name': 'total_turnover', 
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
