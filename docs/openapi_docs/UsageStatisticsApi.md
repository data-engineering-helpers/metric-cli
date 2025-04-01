# openapi_client.UsageStatisticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usage_stats_service_batch_get_usage**](UsageStatisticsApi.md#usage_stats_service_batch_get_usage) | **POST** /api/-/content/usage-stats | Get batch usage statistics
[**usage_stats_service_get_usage_stats**](UsageStatisticsApi.md#usage_stats_service_get_usage_stats) | **GET** /api/-/content/usage-stats/{type}/{luid} | Get usage statistics for content item


# **usage_stats_service_batch_get_usage**
> TableauUsagestatsV1ContentItemUsageStatsList usage_stats_service_batch_get_usage(x_tableau_auth=x_tableau_auth, tableau_usagestats_v1_batch_get_usage_request=tableau_usagestats_v1_batch_get_usage_request)

Get batch usage statistics

Gets usage statistics for multiple content items. The batch of can include multiple content types.

### Example


```python
import openapi_client
from openapi_client.models.tableau_usagestats_v1_batch_get_usage_request import TableauUsagestatsV1BatchGetUsageRequest
from openapi_client.models.tableau_usagestats_v1_content_item_usage_stats_list import TableauUsagestatsV1ContentItemUsageStatsList
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
    api_instance = openapi_client.UsageStatisticsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_usagestats_v1_batch_get_usage_request = openapi_client.TableauUsagestatsV1BatchGetUsageRequest() # TableauUsagestatsV1BatchGetUsageRequest |  (optional)

    try:
        # Get batch usage statistics
        api_response = api_instance.usage_stats_service_batch_get_usage(x_tableau_auth=x_tableau_auth, tableau_usagestats_v1_batch_get_usage_request=tableau_usagestats_v1_batch_get_usage_request)
        print("The response of UsageStatisticsApi->usage_stats_service_batch_get_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageStatisticsApi->usage_stats_service_batch_get_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_usagestats_v1_batch_get_usage_request** | [**TableauUsagestatsV1BatchGetUsageRequest**](TableauUsagestatsV1BatchGetUsageRequest.md)|  | [optional] 

### Return type

[**TableauUsagestatsV1ContentItemUsageStatsList**](TableauUsagestatsV1ContentItemUsageStatsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.usagestats.v1.BatchGetUsageRequest+json
 - **Accept**: application/vnd.tableau.usagestats.v1.ContentItemUsageStatsList+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful. |  -  |
**400** | Invalid Request. The requested was incorrect. |  -  |
**401** | Unable to authenticate user. Credentials are missing or invalid. |  -  |
**500** | Unknown error. There was an internal server error. |  -  |
**404** | Invalid request. The requested resource could not be found. |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_stats_service_get_usage_stats**
> TableauUsagestatsV1UsageStats usage_stats_service_get_usage_stats(type, luid, x_tableau_auth=x_tableau_auth)

Get usage statistics for content item

Gets the usage statistics for a Tableau content item, specified by LUID and content type, such as workbook, datasource, or flow.

### Example


```python
import openapi_client
from openapi_client.models.tableau_usagestats_v1_usage_stats import TableauUsagestatsV1UsageStats
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
    api_instance = openapi_client.UsageStatisticsApi(api_client)
    type = 'type_example' # str | 
    luid = 'luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get usage statistics for content item
        api_response = api_instance.usage_stats_service_get_usage_stats(type, luid, x_tableau_auth=x_tableau_auth)
        print("The response of UsageStatisticsApi->usage_stats_service_get_usage_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageStatisticsApi->usage_stats_service_get_usage_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauUsagestatsV1UsageStats**](TableauUsagestatsV1UsageStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.usagestats.v1.UsageStats+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful. |  -  |
**400** | Usage statistics are not supported for the provided content type. |  -  |
**401** | Unable to authenticate user. Credentials are missing or invalid. |  -  |
**500** | Unknown error. There was an internal server error. |  -  |
**404** | Invalid request. The requested resource could not be found. |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

