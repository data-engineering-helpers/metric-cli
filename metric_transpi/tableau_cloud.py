import json
import requests

import openapi_client


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


    req = requests.api.post(f"https://{host}/api/3.4/auth/signin", headers=headers, json=payload)
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
        return api_response.json()