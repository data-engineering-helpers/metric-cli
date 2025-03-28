import json
import requests
from metric_transpi.dbt import Metric
import openapi_client
from openapi_client.exceptions import ApiException
from openapi_client.models.tableau_metricqueryservice_types_v1_definition import MetricDefinition
from openapi_client.models.tableau_metricqueryservice_v1_create_definition_request import TableauMetricqueryserviceV1CreateDefinitionRequest as create_request
from openapi_client.models.tableau_metricqueryservice_v1_update_definition_request import TableauMetricqueryserviceV1UpdateDefinitionRequest as update_request



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


def list_metric(host: str, api_token: str)-> list[MetricDefinition]:
    configuration = openapi_client.Configuration(
        host = host
    )
    
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.MetricDefinitionsApi(api_client)
        enable_sorting = True 
        x_tableau_auth = api_token
        
        api_response = api_instance.metric_query_service_list_definitions(enable_sorting=enable_sorting, x_tableau_auth=x_tableau_auth)
        return api_response.definitions
    

def create_metric(host: str, api_token: str, definition: MetricDefinition)-> MetricDefinition:
    configuration = openapi_client.Configuration(host = host)
    x_tableau_auth = api_token

    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = openapi_client.MetricDefinitionsApi(api_client)
        api_response = api_instance.metric_query_service_create_definition(
            x_tableau_auth=x_tableau_auth, 
            tableau_metricqueryservice_v1_create_definition_request=create_request(
                name=definition.metadata.name,
                description=definition.metadata.description,
                specification=definition.specification,
                insights_options=definition.insights_options,
                extension_options=definition.extension_options,
                representation_options=definition.representation_options,
                comparisons=definition.comparisons,
            )
        )
        return api_response.definition

def update_metric(host: str, api_token: str, definition: Metric, definition_id: int)-> MetricDefinition:
    
    configuration = openapi_client.Configuration(host = host)
    x_tableau_auth = api_token

    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = openapi_client.MetricDefinitionsApi(api_client)
        api_response = api_instance.metric_query_service_update_definition(
            definition_id=definition_id,
            x_tableau_auth=x_tableau_auth, 
            tableau_metricqueryservice_v1_update_definition_request=update_request(
                definition_id=definition_id,
                name=definition.metadata.name,
                description=definition.metadata.description,
                specification=definition.specification,
                insights_options=definition.insights_options,
                extension_options=definition.extension_options,
                representation_options=definition.representation_options,
                comparisons=definition.comparisons,
            )
        )
        return api_response.definition

class UniquenessViolation(ApiException):
    pass

def match_metric(definitions: list[MetricDefinition], definition: MetricDefinition)-> MetricDefinition:
    for remote_m in definitions:
        if remote_m.metadata.name == definition.metadata.name:
            return remote_m