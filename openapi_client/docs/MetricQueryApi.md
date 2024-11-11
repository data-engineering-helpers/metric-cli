# openapi_client.MetricQueryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metric_query_service_get_entitlements**](MetricQueryApi.md#metric_query_service_get_entitlements) | **GET** /api/-/pulse/entitlements | Get site entitlements


# **metric_query_service_get_entitlements**
> TableauMetricqueryserviceV1GetEntitlementsResponse metric_query_service_get_entitlements(x_tableau_auth=x_tableau_auth)

Get site entitlements

Returns entitlments available for a site.If entitlments are True, then Pulse premium features are enabled for the site.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_get_entitlements_response import TableauMetricqueryserviceV1GetEntitlementsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MetricQueryApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get site entitlements
        api_response = api_instance.metric_query_service_get_entitlements(x_tableau_auth=x_tableau_auth)
        print("The response of MetricQueryApi->metric_query_service_get_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricQueryApi->metric_query_service_get_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1GetEntitlementsResponse**](TableauMetricqueryserviceV1GetEntitlementsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.GetEntitlementsResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful. |  -  |
**400** | Invalid Request. The requested was incorrect. |  -  |
**401** | Unable to authenticate user. Credentials are missing or invalid. |  -  |
**500** | Unknown error. There was an internal server error. |  -  |
**404** | Bad Request. The requested resource could not be found. |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

