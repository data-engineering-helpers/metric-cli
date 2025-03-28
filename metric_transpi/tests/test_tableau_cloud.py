
import requests
import json
from unittest.mock import MagicMock, Mock, call, patch
from metric_transpi.dbt import CalculationMethod, Metric, TimeGrains
from metric_transpi.tableau_cloud import create_metric, list_metric, signin, update_metric
from metric_transpi.translate import to_pulse
from openapi_client.models.tableau_metricqueryservice_types_v1_definition import MetricDefinition
from openapi_client.models.tableau_metricqueryservice_types_v1_metadata import MetricDefinitionMetadata
from openapi_client.models.tableau_metricqueryservice_v1_create_definition_request import TableauMetricqueryserviceV1CreateDefinitionRequest
from openapi_client.models.tableau_metricqueryservice_v1_list_definitions_response import TableauMetricqueryserviceV1ListDefinitionsResponse
from openapi_client.models.tableau_metricqueryservice_v1_update_definition_request import TableauMetricqueryserviceV1UpdateDefinitionRequest

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
    mock_openapi.return_value = TableauMetricqueryserviceV1ListDefinitionsResponse(
        definitions=[
            MetricDefinition(metadata=MetricDefinitionMetadata(name="toto"))
        ]
    )
    
    # When
    definitions = list_metric(
        host=host, 
        api_token=fake_token
    )

    # Then
    assert mock_openapi.call_args == call(x_tableau_auth=fake_token, enable_sorting=True)
    assert definitions[0].metadata.name == "toto"

@patch("openapi_client.api.metric_definitions_api.MetricDefinitionsApi.metric_query_service_create_definition")
def test_create_metric(mock_openapi):
    # Given
    metric = Metric(name="turnover", model="dbt_model_sales", expression="amount", timestamp="transaction_date", 
                    calculation_method="sum", time_grains=[TimeGrains.DAY], dimensions=["country", "store"])
    definition = to_pulse(metric)
    host = "tableau-api-host.toto"
    fake_token = "fake"
    req = TableauMetricqueryserviceV1CreateDefinitionRequest(
        name=definition.metadata.name,
                description=definition.metadata.description,
                specification=definition.specification,
                insights_options=definition.insights_options,
                extension_options=definition.extension_options,
                representation_options=definition.representation_options,
                comparisons=definition.comparisons,
    )
    
    # When
    _ = create_metric(host=host, api_token=fake_token, definition=definition)

    # Then
    mock_openapi.assert_called_once_with(x_tableau_auth=fake_token, tableau_metricqueryservice_v1_create_definition_request=req)

@patch("openapi_client.api.metric_definitions_api.MetricDefinitionsApi.metric_query_service_update_definition")
def test_update_metric(update_def_mock):
    # Given
    definition_id = '#1'
    metric = Metric(name="turnover", model="dbt_model_sales", expression="amount", timestamp="transaction_date", 
                    calculation_method="sum", time_grains=[TimeGrains.DAY], dimensions=["country", "store"])
    definition = to_pulse(metric)
    host = "tableau-api-host.toto"
    fake_token = "fake"
    req = TableauMetricqueryserviceV1UpdateDefinitionRequest(
        definition_id=definition_id,
        name=definition.metadata.name,
        description=definition.metadata.description,
        specification=definition.specification,
        insights_options=definition.insights_options,
        extension_options=definition.extension_options,
        representation_options=definition.representation_options,
        comparisons=definition.comparisons,
    )
    
    # When
    _ = update_metric(host=host, api_token=fake_token, definition=definition, definition_id=definition_id)

    # Then
    update_def_mock.assert_called_once_with(definition_id=definition_id, x_tableau_auth=fake_token, tableau_metricqueryservice_v1_update_definition_request=req)


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
