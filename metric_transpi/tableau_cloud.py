import json
import requests
from metric_transpi.dbt import Metric
from metric_transpi.tableau import TableauAggregation, TableauGranularity
import openapi_client
from openapi_client.models.tableau_metricqueryservice_types_v1_basic_specification import TableauMetricqueryserviceTypesV1BasicSpecification as basic_spec
from openapi_client.models.tableau_metricqueryservice_types_v1_datasource import TableauMetricqueryserviceTypesV1Datasource as datasource
from openapi_client.models.tableau_metricqueryservice_types_v1_definition_specification import TableauMetricqueryserviceTypesV1DefinitionSpecification as def_spec
from openapi_client.models.tableau_metricqueryservice_types_v1_insights_options import TableauMetricqueryserviceTypesV1InsightsOptions as insights_opt
from openapi_client.models.tableau_metricqueryservice_v1_create_definition_request import TableauMetricqueryserviceV1CreateDefinitionRequest as create_def
from openapi_client.models.tableau_metricqueryservice_types_v1_extension_options import TableauMetricqueryserviceTypesV1ExtensionOptions as extension
from openapi_client.models.tableau_metricqueryservice_types_v1_representation_options import TableauMetricqueryserviceTypesV1RepresentationOptions as representation_opt
from openapi_client.models.tableau_metricqueryservice_types_v1_measure import TableauMetricqueryserviceTypesV1Measure as measure
from openapi_client.models.tableau_metricqueryservice_types_v1_time_dimension import TableauMetricqueryserviceTypesV1TimeDimension as time_dim
from openapi_client.models.tableau_metricqueryservice_types_v1_compare_config import TableauMetricqueryserviceTypesV1CompareConfig
from openapi_client.models.tableau_metricqueryservice_types_v1_comparisons import TableauMetricqueryserviceTypesV1Comparisons
from openapi_client.models.tableau_metricqueryservice_types_v1_comparisons_comparison import TableauMetricqueryserviceTypesV1ComparisonsComparison


def signin(
        host: str, 
        site_url_id: str, 
        pat_token_name: str, 
        pat_token_secret: str
    )-> tuple:
    """Signin to Tableau Cloud

    Args:
        host (str): _description_
        site_url_id (str): _description_
        pat_token_name (str): _description_
        pat_token_secret (str): _description_

    Returns:
        token: the API token associated for a session of 1 hour long
        site_id: the uid corresponding to the site_url, usefull to query datasources

    """
    
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    payload = { 
        "credentials": { 
            "personalAccessTokenName": pat_token_name, 
            "personalAccessTokenSecret": pat_token_secret, 
            "site": {"contentUrl": site_url_id }}}

    req = requests.api.post(f"https://{host}/api/3.24/auth/signin", headers=headers, json=payload)
    req.raise_for_status()
    response = json.loads(req.content)
    token = response["credentials"]["token"]
    site_id = response["credentials"]["site"]["id"]

    return (token, site_id)


def list_metric(host: str, api_token: str)-> str:
    configuration = openapi_client.Configuration(
        host = host
    )
    
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.MetricDefinitionsApi(api_client)
        enable_sorting = True 
        x_tableau_auth = api_token
        
        api_response = api_instance.metric_query_service_list_definitions(enable_sorting=enable_sorting, x_tableau_auth=x_tableau_auth)
        return api_response.to_json()
    

def create_metric(host: str, api_token: str, metric: Metric)-> str:
    definition = from_metric_to_metricdef(metric)
    configuration = openapi_client.Configuration(host = host)
    x_tableau_auth = api_token

    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = openapi_client.MetricDefinitionsApi(api_client)
        api_response = api_instance.metric_query_service_create_definition(
            x_tableau_auth=x_tableau_auth, 
            tableau_metricqueryservice_v1_create_definition_request=definition
        )
        return api_response


def from_metric_to_metricdef(metric: Metric):
    definition = create_def(
        name=metric.name,
        specification=def_spec(
            datasource=datasource(
                id=metric.datasource_id
            ),
            basic_specification=basic_spec(
                measure=measure(
                    var_field=metric.expression,
                    aggregation=TableauAggregation[metric.calculation_method.name].value
                ),
                time_dimension=time_dim(
                    field=metric.timestamp,
                )
            ),
            is_running_total=True
        ),
        extension_options=extension(
            allowed_dimensions=metric.dimensions,
            allowed_granularities=[TableauGranularity[grain.name].value for grain in metric.time_grains]
        ),
        representation_options=representation_opt(),
        insights_options=insights_opt(),
        comparisons=TableauMetricqueryserviceTypesV1Comparisons(
            comparisons=[
                TableauMetricqueryserviceTypesV1ComparisonsComparison(
                    compare_config=TableauMetricqueryserviceTypesV1CompareConfig(
                        comparison='TIME_COMPARISON_PREVIOUS_PERIOD'
                    )
            )]
        )
    ) 
    return definition