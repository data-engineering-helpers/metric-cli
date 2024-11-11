# openapi_client.MetricDefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metric_query_service_batch_get_definitions**](MetricDefinitionsApi.md#metric_query_service_batch_get_definitions) | **GET** /api/-/pulse/definitions:batchGet | Gets a batch of definition and metrics available on a server.
[**metric_query_service_batch_get_definitions_by_post**](MetricDefinitionsApi.md#metric_query_service_batch_get_definitions_by_post) | **POST** /api/-/pulse/definitions:batchGet | Gets a batch of definition and metrics available on a server.
[**metric_query_service_batch_get_metrics**](MetricDefinitionsApi.md#metric_query_service_batch_get_metrics) | **GET** /api/-/pulse/metrics:batchGet | Gets a batch of metrics available on a server.
[**metric_query_service_create_definition**](MetricDefinitionsApi.md#metric_query_service_create_definition) | **POST** /api/-/pulse/definitions | Creates a metric definition.
[**metric_query_service_create_metric**](MetricDefinitionsApi.md#metric_query_service_create_metric) | **POST** /api/-/pulse/metrics | Creates a metric.
[**metric_query_service_delete_definition**](MetricDefinitionsApi.md#metric_query_service_delete_definition) | **DELETE** /api/-/pulse/definitions/{definition_id} | Deletes a metric definition.
[**metric_query_service_delete_metric**](MetricDefinitionsApi.md#metric_query_service_delete_metric) | **DELETE** /api/-/pulse/metrics/{metric_id} | Deletes a metric.
[**metric_query_service_get_definition**](MetricDefinitionsApi.md#metric_query_service_get_definition) | **GET** /api/-/pulse/definitions/{definition_id} | Gets a metric definition based on the specified id.
[**metric_query_service_get_metric**](MetricDefinitionsApi.md#metric_query_service_get_metric) | **GET** /api/-/pulse/metrics/{metric_id} | Gets the metric by ID.
[**metric_query_service_get_or_create_metric**](MetricDefinitionsApi.md#metric_query_service_get_or_create_metric) | **POST** /api/-/pulse/metrics:getOrCreate | Creates a metric and returns boolean indicating whether the new metric was created or not.
[**metric_query_service_list_definitions**](MetricDefinitionsApi.md#metric_query_service_list_definitions) | **GET** /api/-/pulse/definitions | Lists the definitions available on a server.
[**metric_query_service_list_metrics**](MetricDefinitionsApi.md#metric_query_service_list_metrics) | **GET** /api/-/pulse/definitions/{definition_id}/metrics | Lists the metrics available on a server.
[**metric_query_service_update_definition**](MetricDefinitionsApi.md#metric_query_service_update_definition) | **PATCH** /api/-/pulse/definitions/{definition_id} | Updates a metric definition.
[**metric_query_service_update_metric**](MetricDefinitionsApi.md#metric_query_service_update_metric) | **PATCH** /api/-/pulse/metrics/{metric_id} | Updates a metric.
[**pulse_subscription_service_list_followed_metrics_groups**](MetricDefinitionsApi.md#pulse_subscription_service_list_followed_metrics_groups) | **GET** /api/-/pulse/metrics:followedMetricsGroups | List followed metrics groups


# **metric_query_service_batch_get_definitions**
> TableauMetricqueryserviceV1BatchGetDefinitionsResponse metric_query_service_batch_get_definitions(definition_ids=definition_ids, view=view, x_tableau_auth=x_tableau_auth, number_of_metrics=number_of_metrics)

Gets a batch of definition and metrics available on a server.

Gets batches of definitions and metrics available on a server. Only metrics a user has privileges to view will be visible.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_batch_get_definitions_response import TableauMetricqueryserviceV1BatchGetDefinitionsResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    definition_ids = 'definition_ids_example' # str |  (optional)
    view = 'view_example' # str |  (optional)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    number_of_metrics = 56 # int |  (optional)

    try:
        # Gets a batch of definition and metrics available on a server.
        api_response = api_instance.metric_query_service_batch_get_definitions(definition_ids=definition_ids, view=view, x_tableau_auth=x_tableau_auth, number_of_metrics=number_of_metrics)
        print("The response of MetricDefinitionsApi->metric_query_service_batch_get_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_batch_get_definitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_ids** | **str**|  | [optional] 
 **view** | **str**|  | [optional] 
 **x_tableau_auth** | **str**|  | [optional] 
 **number_of_metrics** | **int**|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1BatchGetDefinitionsResponse**](TableauMetricqueryserviceV1BatchGetDefinitionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.BatchGetDefinitionsResponse+json, application/json

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

# **metric_query_service_batch_get_definitions_by_post**
> TableauMetricqueryserviceV1BatchGetDefinitionsByPostResponse metric_query_service_batch_get_definitions_by_post(x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_batch_get_definitions_by_post_request=tableau_metricqueryservice_v1_batch_get_definitions_by_post_request)

Gets a batch of definition and metrics available on a server.

Gets batches of definitions and metrics available on a server. Only metrics a user has privileges to view will be visible.  This endpoint uses POST as an alternative to GET, where long lists of URL parameters could be problematic.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_batch_get_definitions_by_post_request import TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest
from openapi_client.models.tableau_metricqueryservice_v1_batch_get_definitions_by_post_response import TableauMetricqueryserviceV1BatchGetDefinitionsByPostResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_metricqueryservice_v1_batch_get_definitions_by_post_request = openapi_client.TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest() # TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest |  (optional)

    try:
        # Gets a batch of definition and metrics available on a server.
        api_response = api_instance.metric_query_service_batch_get_definitions_by_post(x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_batch_get_definitions_by_post_request=tableau_metricqueryservice_v1_batch_get_definitions_by_post_request)
        print("The response of MetricDefinitionsApi->metric_query_service_batch_get_definitions_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_batch_get_definitions_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_metricqueryservice_v1_batch_get_definitions_by_post_request** | [**TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest**](TableauMetricqueryserviceV1BatchGetDefinitionsByPostRequest.md)|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1BatchGetDefinitionsByPostResponse**](TableauMetricqueryserviceV1BatchGetDefinitionsByPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.metricqueryservice.v1.BatchGetDefinitionsByPostRequest+json
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.BatchGetDefinitionsByPostResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful. |  -  |
**400** | Invalid Request. The requested was incorrect. |  -  |
**401** | Unable to authenticate user. Credentials are missing or invalid. |  -  |
**500** | Unknown error. There was an internal server error. |  -  |
**404** | Bad Request. The requested resource could not be found. |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_query_service_batch_get_metrics**
> TableauMetricqueryserviceV1BatchGetMetricsResponse metric_query_service_batch_get_metrics(enable_sorting=enable_sorting, x_tableau_auth=x_tableau_auth, metric_ids=metric_ids)

Gets a batch of metrics available on a server.

Gets batches of metrics available on a server. Only metrics a user has privileges to view will be visible.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_batch_get_metrics_response import TableauMetricqueryserviceV1BatchGetMetricsResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    enable_sorting = True # bool |  (optional)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    metric_ids = 'metric_ids_example' # str |  (optional)

    try:
        # Gets a batch of metrics available on a server.
        api_response = api_instance.metric_query_service_batch_get_metrics(enable_sorting=enable_sorting, x_tableau_auth=x_tableau_auth, metric_ids=metric_ids)
        print("The response of MetricDefinitionsApi->metric_query_service_batch_get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_batch_get_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_sorting** | **bool**|  | [optional] 
 **x_tableau_auth** | **str**|  | [optional] 
 **metric_ids** | **str**|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1BatchGetMetricsResponse**](TableauMetricqueryserviceV1BatchGetMetricsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.BatchGetMetricsResponse+json, application/json

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

# **metric_query_service_create_definition**
> TableauMetricqueryserviceV1CreateDefinitionResponse metric_query_service_create_definition(x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_create_definition_request=tableau_metricqueryservice_v1_create_definition_request)

Creates a metric definition.

Creates a metric definition.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_create_definition_request import TableauMetricqueryserviceV1CreateDefinitionRequest
from openapi_client.models.tableau_metricqueryservice_v1_create_definition_response import TableauMetricqueryserviceV1CreateDefinitionResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_metricqueryservice_v1_create_definition_request = openapi_client.TableauMetricqueryserviceV1CreateDefinitionRequest() # TableauMetricqueryserviceV1CreateDefinitionRequest |  (optional)

    try:
        # Creates a metric definition.
        api_response = api_instance.metric_query_service_create_definition(x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_create_definition_request=tableau_metricqueryservice_v1_create_definition_request)
        print("The response of MetricDefinitionsApi->metric_query_service_create_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_create_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_metricqueryservice_v1_create_definition_request** | [**TableauMetricqueryserviceV1CreateDefinitionRequest**](TableauMetricqueryserviceV1CreateDefinitionRequest.md)|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1CreateDefinitionResponse**](TableauMetricqueryserviceV1CreateDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.metricqueryservice.v1.CreateDefinitionRequest+json
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.CreateDefinitionResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful. |  -  |
**400** | Invalid Request. The requested was incorrect. |  -  |
**401** | Unable to authenticate user. Credentials are missing or invalid. |  -  |
**500** | Unknown error. There was an internal server error. |  -  |
**404** | Bad Request. The requested resource could not be found. |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_query_service_create_metric**
> TableauMetricqueryserviceV1CreateMetricResponse metric_query_service_create_metric(x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_create_metric_request=tableau_metricqueryservice_v1_create_metric_request)

Creates a metric.

Creates a metric.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_create_metric_request import TableauMetricqueryserviceV1CreateMetricRequest
from openapi_client.models.tableau_metricqueryservice_v1_create_metric_response import TableauMetricqueryserviceV1CreateMetricResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_metricqueryservice_v1_create_metric_request = openapi_client.TableauMetricqueryserviceV1CreateMetricRequest() # TableauMetricqueryserviceV1CreateMetricRequest |  (optional)

    try:
        # Creates a metric.
        api_response = api_instance.metric_query_service_create_metric(x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_create_metric_request=tableau_metricqueryservice_v1_create_metric_request)
        print("The response of MetricDefinitionsApi->metric_query_service_create_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_create_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_metricqueryservice_v1_create_metric_request** | [**TableauMetricqueryserviceV1CreateMetricRequest**](TableauMetricqueryserviceV1CreateMetricRequest.md)|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1CreateMetricResponse**](TableauMetricqueryserviceV1CreateMetricResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.metricqueryservice.v1.CreateMetricRequest+json
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.CreateMetricResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful. |  -  |
**400** | Invalid Request. The requested was incorrect. |  -  |
**401** | Unable to authenticate user. Credentials are missing or invalid. |  -  |
**500** | Unknown error. There was an internal server error. |  -  |
**404** | Bad Request. The requested resource could not be found. |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_query_service_delete_definition**
> metric_query_service_delete_definition(definition_id, x_tableau_auth=x_tableau_auth)

Deletes a metric definition.

Deletes a metric definition.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    definition_id = 'definition_id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Deletes a metric definition.
        api_instance.metric_query_service_delete_definition(definition_id, x_tableau_auth=x_tableau_auth)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_delete_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Empty Response Body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_query_service_delete_metric**
> metric_query_service_delete_metric(metric_id, x_tableau_auth=x_tableau_auth)

Deletes a metric.

Deletes a metric.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    metric_id = 'metric_id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Deletes a metric.
        api_instance.metric_query_service_delete_metric(metric_id, x_tableau_auth=x_tableau_auth)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_delete_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Empty Response Body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_query_service_get_definition**
> TableauMetricqueryserviceV1GetDefinitionResponse metric_query_service_get_definition(definition_id, view=view, x_tableau_auth=x_tableau_auth, number_of_metrics=number_of_metrics)

Gets a metric definition based on the specified id.

Gets a metric definition and potentially metrics based off it based on the id.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_get_definition_response import TableauMetricqueryserviceV1GetDefinitionResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    definition_id = 'definition_id_example' # str | 
    view = 'view_example' # str |  (optional)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    number_of_metrics = 56 # int |  (optional)

    try:
        # Gets a metric definition based on the specified id.
        api_response = api_instance.metric_query_service_get_definition(definition_id, view=view, x_tableau_auth=x_tableau_auth, number_of_metrics=number_of_metrics)
        print("The response of MetricDefinitionsApi->metric_query_service_get_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_get_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_id** | **str**|  | 
 **view** | **str**|  | [optional] 
 **x_tableau_auth** | **str**|  | [optional] 
 **number_of_metrics** | **int**|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1GetDefinitionResponse**](TableauMetricqueryserviceV1GetDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.GetDefinitionResponse+json, application/json

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

# **metric_query_service_get_metric**
> TableauMetricqueryserviceV1GetMetricResponse metric_query_service_get_metric(metric_id, x_tableau_auth=x_tableau_auth)

Gets the metric by ID.

Gets the metric by its ID. User must have privileges to view the requested metric.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_get_metric_response import TableauMetricqueryserviceV1GetMetricResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    metric_id = 'metric_id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Gets the metric by ID.
        api_response = api_instance.metric_query_service_get_metric(metric_id, x_tableau_auth=x_tableau_auth)
        print("The response of MetricDefinitionsApi->metric_query_service_get_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_get_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1GetMetricResponse**](TableauMetricqueryserviceV1GetMetricResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.GetMetricResponse+json, application/json

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

# **metric_query_service_get_or_create_metric**
> TableauMetricqueryserviceV1GetOrCreateMetricResponse metric_query_service_get_or_create_metric(x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_get_or_create_metric_request=tableau_metricqueryservice_v1_get_or_create_metric_request)

Creates a metric and returns boolean indicating whether the new metric was created or not.

Creates a metric and returns boolean indicating whether the new metric was created or not.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_get_or_create_metric_request import TableauMetricqueryserviceV1GetOrCreateMetricRequest
from openapi_client.models.tableau_metricqueryservice_v1_get_or_create_metric_response import TableauMetricqueryserviceV1GetOrCreateMetricResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_metricqueryservice_v1_get_or_create_metric_request = openapi_client.TableauMetricqueryserviceV1GetOrCreateMetricRequest() # TableauMetricqueryserviceV1GetOrCreateMetricRequest |  (optional)

    try:
        # Creates a metric and returns boolean indicating whether the new metric was created or not.
        api_response = api_instance.metric_query_service_get_or_create_metric(x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_get_or_create_metric_request=tableau_metricqueryservice_v1_get_or_create_metric_request)
        print("The response of MetricDefinitionsApi->metric_query_service_get_or_create_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_get_or_create_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_metricqueryservice_v1_get_or_create_metric_request** | [**TableauMetricqueryserviceV1GetOrCreateMetricRequest**](TableauMetricqueryserviceV1GetOrCreateMetricRequest.md)|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1GetOrCreateMetricResponse**](TableauMetricqueryserviceV1GetOrCreateMetricResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.metricqueryservice.v1.GetOrCreateMetricRequest+json
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.GetOrCreateMetricResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful. |  -  |
**400** | Invalid Request. The requested was incorrect. |  -  |
**401** | Unable to authenticate user. Credentials are missing or invalid. |  -  |
**500** | Unknown error. There was an internal server error. |  -  |
**404** | Bad Request. The requested resource could not be found. |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_query_service_list_definitions**
> TableauMetricqueryserviceV1ListDefinitionsResponse metric_query_service_list_definitions(enable_sorting=enable_sorting, order_by=order_by, view=view, x_tableau_auth=x_tableau_auth, page_size=page_size, exclude_metrics_without_followers=exclude_metrics_without_followers, filter=filter, metric_id=metric_id, number_of_metrics=number_of_metrics, page_token=page_token)

Lists the definitions available on a server.

Lists the definitions and metrics available on a server. Only definitions a user has privileges to view will be visible.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_list_definitions_response import TableauMetricqueryserviceV1ListDefinitionsResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    enable_sorting = True # bool |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    view = 'view_example' # str |  (optional)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    page_size = 56 # int | Specifies the number of results in a paged response.   Example:   > `GET ...//definitions?pageSize=50`   Combining Path Parameters:  A page_size expression can be combined with other path parameters using an ampersand (&) as a separator, and is typically used along with a page number expression.   <a href='https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm' target='_blank'>Learn more about paginating the response</a>. (optional)
    exclude_metrics_without_followers = True # bool |  (optional)
    filter = 'filter_example' # str |  (optional)
    metric_id = 'metric_id_example' # str |  (optional)
    number_of_metrics = 56 # int |  (optional)
    page_token = 'page_token_example' # str | Specifies the page of items to be returned from a requested list. The value of `page_token` for the next page of returns is found in the `next_page_token` of the current response. If there are no further items to return, the value of `next_page_token` will be empty.  Example:  > `GET ...//definitions?pageToken={next_page_value}` Combining Path Parameters:  A page_token expression can be combined with other path parameters using an ampersand (&) as a separator, and is typically used along with a page number expression.   <a href='https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm' target='_blank'>Learn more about paginating the response</a>. (optional)

    try:
        # Lists the definitions available on a server.
        api_response = api_instance.metric_query_service_list_definitions(enable_sorting=enable_sorting, order_by=order_by, view=view, x_tableau_auth=x_tableau_auth, page_size=page_size, exclude_metrics_without_followers=exclude_metrics_without_followers, filter=filter, metric_id=metric_id, number_of_metrics=number_of_metrics, page_token=page_token)
        print("The response of MetricDefinitionsApi->metric_query_service_list_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_list_definitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_sorting** | **bool**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **view** | **str**|  | [optional] 
 **x_tableau_auth** | **str**|  | [optional] 
 **page_size** | **int**| Specifies the number of results in a paged response.   Example:   &gt; &#x60;GET ...//definitions?pageSize&#x3D;50&#x60;   Combining Path Parameters:  A page_size expression can be combined with other path parameters using an ampersand (&amp;) as a separator, and is typically used along with a page number expression.   &lt;a href&#x3D;&#39;https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Learn more about paginating the response&lt;/a&gt;. | [optional] 
 **exclude_metrics_without_followers** | **bool**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **metric_id** | **str**|  | [optional] 
 **number_of_metrics** | **int**|  | [optional] 
 **page_token** | **str**| Specifies the page of items to be returned from a requested list. The value of &#x60;page_token&#x60; for the next page of returns is found in the &#x60;next_page_token&#x60; of the current response. If there are no further items to return, the value of &#x60;next_page_token&#x60; will be empty.  Example:  &gt; &#x60;GET ...//definitions?pageToken&#x3D;{next_page_value}&#x60; Combining Path Parameters:  A page_token expression can be combined with other path parameters using an ampersand (&amp;) as a separator, and is typically used along with a page number expression.   &lt;a href&#x3D;&#39;https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Learn more about paginating the response&lt;/a&gt;. | [optional] 

### Return type

[**TableauMetricqueryserviceV1ListDefinitionsResponse**](TableauMetricqueryserviceV1ListDefinitionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.ListDefinitionsResponse+json, application/json

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

# **metric_query_service_list_metrics**
> TableauMetricqueryserviceV1ListMetricsResponse metric_query_service_list_metrics(definition_id, page_size=page_size, page_token=page_token, enable_sorting=enable_sorting, order_by=order_by, x_tableau_auth=x_tableau_auth, exclude_metrics_without_followers=exclude_metrics_without_followers, filter=filter)

Lists the metrics available on a server.

Lists the metrics based on a metric definition. Only metrics a user has privileges to view will be visible.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_list_metrics_response import TableauMetricqueryserviceV1ListMetricsResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    definition_id = 'definition_id_example' # str | 
    page_size = 56 # int | Specifies the number of results in a paged response.   Example:   > `GET ...//definitions/{definition_id}/metrics?pageSize=50`   Combining Path Parameters:  A page_size expression can be combined with other path parameters using an ampersand (&) as a separator, and is typically used along with a page number expression.   <a href='https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm' target='_blank'>Learn more about paginating the response</a>. (optional)
    page_token = 'page_token_example' # str | Specifies the page of items to be returned from a requested list. The value of `page_token` for the next page of returns is found in the `next_page_token` of the current response. If there are no further items to return, the value of `next_page_token` will be empty.  Example:  > `GET ...//definitions/{definition_id}/metrics?pageToken={next_page_value}` Combining Path Parameters:  A page_token expression can be combined with other path parameters using an ampersand (&) as a separator, and is typically used along with a page number expression.   <a href='https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm' target='_blank'>Learn more about paginating the response</a>. (optional)
    enable_sorting = True # bool |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    exclude_metrics_without_followers = True # bool |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # Lists the metrics available on a server.
        api_response = api_instance.metric_query_service_list_metrics(definition_id, page_size=page_size, page_token=page_token, enable_sorting=enable_sorting, order_by=order_by, x_tableau_auth=x_tableau_auth, exclude_metrics_without_followers=exclude_metrics_without_followers, filter=filter)
        print("The response of MetricDefinitionsApi->metric_query_service_list_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_list_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_id** | **str**|  | 
 **page_size** | **int**| Specifies the number of results in a paged response.   Example:   &gt; &#x60;GET ...//definitions/{definition_id}/metrics?pageSize&#x3D;50&#x60;   Combining Path Parameters:  A page_size expression can be combined with other path parameters using an ampersand (&amp;) as a separator, and is typically used along with a page number expression.   &lt;a href&#x3D;&#39;https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Learn more about paginating the response&lt;/a&gt;. | [optional] 
 **page_token** | **str**| Specifies the page of items to be returned from a requested list. The value of &#x60;page_token&#x60; for the next page of returns is found in the &#x60;next_page_token&#x60; of the current response. If there are no further items to return, the value of &#x60;next_page_token&#x60; will be empty.  Example:  &gt; &#x60;GET ...//definitions/{definition_id}/metrics?pageToken&#x3D;{next_page_value}&#x60; Combining Path Parameters:  A page_token expression can be combined with other path parameters using an ampersand (&amp;) as a separator, and is typically used along with a page number expression.   &lt;a href&#x3D;&#39;https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Learn more about paginating the response&lt;/a&gt;. | [optional] 
 **enable_sorting** | **bool**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **x_tableau_auth** | **str**|  | [optional] 
 **exclude_metrics_without_followers** | **bool**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1ListMetricsResponse**](TableauMetricqueryserviceV1ListMetricsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.ListMetricsResponse+json, application/json

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

# **metric_query_service_update_definition**
> TableauMetricqueryserviceV1UpdateDefinitionResponse metric_query_service_update_definition(definition_id, x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_update_definition_request=tableau_metricqueryservice_v1_update_definition_request)

Updates a metric definition.

Updates a metric definition.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_update_definition_request import TableauMetricqueryserviceV1UpdateDefinitionRequest
from openapi_client.models.tableau_metricqueryservice_v1_update_definition_response import TableauMetricqueryserviceV1UpdateDefinitionResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    definition_id = 'definition_id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_metricqueryservice_v1_update_definition_request = openapi_client.TableauMetricqueryserviceV1UpdateDefinitionRequest() # TableauMetricqueryserviceV1UpdateDefinitionRequest |  (optional)

    try:
        # Updates a metric definition.
        api_response = api_instance.metric_query_service_update_definition(definition_id, x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_update_definition_request=tableau_metricqueryservice_v1_update_definition_request)
        print("The response of MetricDefinitionsApi->metric_query_service_update_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_update_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_metricqueryservice_v1_update_definition_request** | [**TableauMetricqueryserviceV1UpdateDefinitionRequest**](TableauMetricqueryserviceV1UpdateDefinitionRequest.md)|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1UpdateDefinitionResponse**](TableauMetricqueryserviceV1UpdateDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.metricqueryservice.v1.UpdateDefinitionRequest+json
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.UpdateDefinitionResponse+json, application/json

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

# **metric_query_service_update_metric**
> TableauMetricqueryserviceV1UpdateMetricResponse metric_query_service_update_metric(metric_id, x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_update_metric_request=tableau_metricqueryservice_v1_update_metric_request)

Updates a metric.

Updates a metric.

### Example


```python
import openapi_client
from openapi_client.models.tableau_metricqueryservice_v1_update_metric_request import TableauMetricqueryserviceV1UpdateMetricRequest
from openapi_client.models.tableau_metricqueryservice_v1_update_metric_response import TableauMetricqueryserviceV1UpdateMetricResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    metric_id = 'metric_id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_metricqueryservice_v1_update_metric_request = openapi_client.TableauMetricqueryserviceV1UpdateMetricRequest() # TableauMetricqueryserviceV1UpdateMetricRequest |  (optional)

    try:
        # Updates a metric.
        api_response = api_instance.metric_query_service_update_metric(metric_id, x_tableau_auth=x_tableau_auth, tableau_metricqueryservice_v1_update_metric_request=tableau_metricqueryservice_v1_update_metric_request)
        print("The response of MetricDefinitionsApi->metric_query_service_update_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->metric_query_service_update_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_metricqueryservice_v1_update_metric_request** | [**TableauMetricqueryserviceV1UpdateMetricRequest**](TableauMetricqueryserviceV1UpdateMetricRequest.md)|  | [optional] 

### Return type

[**TableauMetricqueryserviceV1UpdateMetricResponse**](TableauMetricqueryserviceV1UpdateMetricResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.metricqueryservice.v1.UpdateMetricRequest+json
 - **Accept**: application/vnd.tableau.metricqueryservice.v1.UpdateMetricResponse+json, application/json

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

# **pulse_subscription_service_list_followed_metrics_groups**
> TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse pulse_subscription_service_list_followed_metrics_groups(x_tableau_auth=x_tableau_auth, sort_order=sort_order, group_by=group_by)

List followed metrics groups

Gets the user's followed metrics. Optionally metrics can be grouped by characteristics like datasource, and sorted. If no grouping and sorting is specified then returns are grouped and sorted by existing user preferences. If no user preferences exist or are specified, then metrics are grouped by most recently followed, in descending order. If metrics are grouped by most recently followed then they are returned in a single group, that is sorted by the specified, existing, or default order.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_list_followed_metrics_groups_response import TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse
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
    api_instance = openapi_client.MetricDefinitionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    sort_order = 'sort_order_example' # str |  (optional)
    group_by = 'group_by_example' # str |  (optional)

    try:
        # List followed metrics groups
        api_response = api_instance.pulse_subscription_service_list_followed_metrics_groups(x_tableau_auth=x_tableau_auth, sort_order=sort_order, group_by=group_by)
        print("The response of MetricDefinitionsApi->pulse_subscription_service_list_followed_metrics_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricDefinitionsApi->pulse_subscription_service_list_followed_metrics_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **group_by** | **str**|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse**](TableauPulseSubscriptionserviceV1ListFollowedMetricsGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.ListFollowedMetricsGroupsResponse+json, application/json

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

