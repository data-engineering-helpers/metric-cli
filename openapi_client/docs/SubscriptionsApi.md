# openapi_client.SubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pulse_subscription_service_batch_create_subscriptions**](SubscriptionsApi.md#pulse_subscription_service_batch_create_subscriptions) | **POST** /api/-/pulse/subscriptions:batchCreate | Creates multiple subscriptions.
[**pulse_subscription_service_batch_get_metric_follower_counts**](SubscriptionsApi.md#pulse_subscription_service_batch_get_metric_follower_counts) | **GET** /api/-/pulse/subscriptions:batchGetMetricFollowerCounts | Gets the total number of unique followers per metric
[**pulse_subscription_service_batch_get_subscriptions**](SubscriptionsApi.md#pulse_subscription_service_batch_get_subscriptions) | **GET** /api/-/pulse/subscriptions:batchGet | Gets a batch of subscriptions available on a server.
[**pulse_subscription_service_create_subscription**](SubscriptionsApi.md#pulse_subscription_service_create_subscription) | **POST** /api/-/pulse/subscriptions | Creates a subscription.
[**pulse_subscription_service_delete_subscription**](SubscriptionsApi.md#pulse_subscription_service_delete_subscription) | **DELETE** /api/-/pulse/subscriptions/{id} | Deletes a subscription.
[**pulse_subscription_service_get_subscription**](SubscriptionsApi.md#pulse_subscription_service_get_subscription) | **GET** /api/-/pulse/subscriptions/{id} | Gets a subscription based on the specified id.
[**pulse_subscription_service_get_user_digest_preferences**](SubscriptionsApi.md#pulse_subscription_service_get_user_digest_preferences) | **GET** /api/-/pulse/user/digestpreferences | Get user digest preferences
[**pulse_subscription_service_get_user_preferences**](SubscriptionsApi.md#pulse_subscription_service_get_user_preferences) | **GET** /api/-/pulse/user/preferences | Get user preferences
[**pulse_subscription_service_list_subscriptions**](SubscriptionsApi.md#pulse_subscription_service_list_subscriptions) | **GET** /api/-/pulse/subscriptions | Lists the subscriptions available on a server.
[**pulse_subscription_service_update_subscription**](SubscriptionsApi.md#pulse_subscription_service_update_subscription) | **PATCH** /api/-/pulse/subscriptions/{id} | Updates a subscription.
[**pulse_subscription_service_update_user_digest_preferences**](SubscriptionsApi.md#pulse_subscription_service_update_user_digest_preferences) | **PATCH** /api/-/pulse/user/digestpreferences | Update user digest preferences
[**pulse_subscription_service_update_user_preferences**](SubscriptionsApi.md#pulse_subscription_service_update_user_preferences) | **PATCH** /api/-/pulse/user/preferences | Update user preferences


# **pulse_subscription_service_batch_create_subscriptions**
> TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse pulse_subscription_service_batch_create_subscriptions(x_tableau_auth=x_tableau_auth, tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request=tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request)

Creates multiple subscriptions.

Creates multiple subscriptions.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request import TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest
from openapi_client.models.tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_response import TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request = openapi_client.TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest() # TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest |  (optional)

    try:
        # Creates multiple subscriptions.
        api_response = api_instance.pulse_subscription_service_batch_create_subscriptions(x_tableau_auth=x_tableau_auth, tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request=tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request)
        print("The response of SubscriptionsApi->pulse_subscription_service_batch_create_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_batch_create_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_pulse_subscriptionservice_v1_batch_create_subscriptions_request** | [**TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest**](TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsRequest.md)|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse**](TableauPulseSubscriptionserviceV1BatchCreateSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.pulse.subscriptionservice.v1.BatchCreateSubscriptionsRequest+json
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.BatchCreateSubscriptionsResponse+json, application/json

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

# **pulse_subscription_service_batch_get_metric_follower_counts**
> TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse pulse_subscription_service_batch_get_metric_follower_counts(x_tableau_auth=x_tableau_auth, metric_ids=metric_ids)

Gets the total number of unique followers per metric

Calculates the number of unique followers for list of metrics. For metrics that have group followers the count will be the union of all the members of the subscribed groups plus all the individual followers.  Users are counted only once per metric.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_batch_get_metric_follower_counts_response import TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    metric_ids = 'metric_ids_example' # str |  (optional)

    try:
        # Gets the total number of unique followers per metric
        api_response = api_instance.pulse_subscription_service_batch_get_metric_follower_counts(x_tableau_auth=x_tableau_auth, metric_ids=metric_ids)
        print("The response of SubscriptionsApi->pulse_subscription_service_batch_get_metric_follower_counts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_batch_get_metric_follower_counts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **metric_ids** | **str**|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse**](TableauPulseSubscriptionserviceV1BatchGetMetricFollowerCountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.BatchGetMetricFollowerCountsResponse+json, application/json

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

# **pulse_subscription_service_batch_get_subscriptions**
> TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse pulse_subscription_service_batch_get_subscriptions(x_tableau_auth=x_tableau_auth)

Gets a batch of subscriptions available on a server.

Gets batches of subscriptions available on a server. Only subscriptions a user has privileges to view will be visible.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_batch_get_subscriptions_response import TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Gets a batch of subscriptions available on a server.
        api_response = api_instance.pulse_subscription_service_batch_get_subscriptions(x_tableau_auth=x_tableau_auth)
        print("The response of SubscriptionsApi->pulse_subscription_service_batch_get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_batch_get_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse**](TableauPulseSubscriptionserviceV1BatchGetSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.BatchGetSubscriptionsResponse+json, application/json

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

# **pulse_subscription_service_create_subscription**
> TableauPulseSubscriptionserviceV1CreateSubscriptionResponse pulse_subscription_service_create_subscription(x_tableau_auth=x_tableau_auth, tableau_pulse_subscriptionservice_v1_create_subscription_request=tableau_pulse_subscriptionservice_v1_create_subscription_request)

Creates a subscription.

Creates a subscription.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_create_subscription_request import TableauPulseSubscriptionserviceV1CreateSubscriptionRequest
from openapi_client.models.tableau_pulse_subscriptionservice_v1_create_subscription_response import TableauPulseSubscriptionserviceV1CreateSubscriptionResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_pulse_subscriptionservice_v1_create_subscription_request = openapi_client.TableauPulseSubscriptionserviceV1CreateSubscriptionRequest() # TableauPulseSubscriptionserviceV1CreateSubscriptionRequest |  (optional)

    try:
        # Creates a subscription.
        api_response = api_instance.pulse_subscription_service_create_subscription(x_tableau_auth=x_tableau_auth, tableau_pulse_subscriptionservice_v1_create_subscription_request=tableau_pulse_subscriptionservice_v1_create_subscription_request)
        print("The response of SubscriptionsApi->pulse_subscription_service_create_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_create_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_pulse_subscriptionservice_v1_create_subscription_request** | [**TableauPulseSubscriptionserviceV1CreateSubscriptionRequest**](TableauPulseSubscriptionserviceV1CreateSubscriptionRequest.md)|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1CreateSubscriptionResponse**](TableauPulseSubscriptionserviceV1CreateSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.pulse.subscriptionservice.v1.CreateSubscriptionRequest+json
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.CreateSubscriptionResponse+json, application/json

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

# **pulse_subscription_service_delete_subscription**
> pulse_subscription_service_delete_subscription(id, x_tableau_auth=x_tableau_auth)

Deletes a subscription.

Deletes a subscription.

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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    id = 'id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Deletes a subscription.
        api_instance.pulse_subscription_service_delete_subscription(id, x_tableau_auth=x_tableau_auth)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_delete_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **pulse_subscription_service_get_subscription**
> TableauPulseSubscriptionserviceV1GetSubscriptionResponse pulse_subscription_service_get_subscription(id, x_tableau_auth=x_tableau_auth)

Gets a subscription based on the specified id.

Gets a subscription.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_get_subscription_response import TableauPulseSubscriptionserviceV1GetSubscriptionResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    id = 'id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Gets a subscription based on the specified id.
        api_response = api_instance.pulse_subscription_service_get_subscription(id, x_tableau_auth=x_tableau_auth)
        print("The response of SubscriptionsApi->pulse_subscription_service_get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1GetSubscriptionResponse**](TableauPulseSubscriptionserviceV1GetSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.GetSubscriptionResponse+json, application/json

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

# **pulse_subscription_service_get_user_digest_preferences**
> TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse pulse_subscription_service_get_user_digest_preferences(x_tableau_auth=x_tableau_auth)

Get user digest preferences

Gets the user's digest preferences for which delivery channels to receive notifications on, and at what cadence.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_get_user_digest_preferences_response import TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get user digest preferences
        api_response = api_instance.pulse_subscription_service_get_user_digest_preferences(x_tableau_auth=x_tableau_auth)
        print("The response of SubscriptionsApi->pulse_subscription_service_get_user_digest_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_get_user_digest_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse**](TableauPulseSubscriptionserviceV1GetUserDigestPreferencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.GetUserDigestPreferencesResponse+json, application/json

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

# **pulse_subscription_service_get_user_preferences**
> TableauPulseSubscriptionserviceV1GetUserPreferencesResponse pulse_subscription_service_get_user_preferences(x_tableau_auth=x_tableau_auth)

Get user preferences

Gets the user's preferences for notifications channels and cadence, and for grouping and sorting followed metrics in REST responses and UI.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_get_user_preferences_response import TableauPulseSubscriptionserviceV1GetUserPreferencesResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get user preferences
        api_response = api_instance.pulse_subscription_service_get_user_preferences(x_tableau_auth=x_tableau_auth)
        print("The response of SubscriptionsApi->pulse_subscription_service_get_user_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_get_user_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1GetUserPreferencesResponse**](TableauPulseSubscriptionserviceV1GetUserPreferencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.GetUserPreferencesResponse+json, application/json

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

# **pulse_subscription_service_list_subscriptions**
> TableauPulseSubscriptionserviceV1ListSubscriptionsResponse pulse_subscription_service_list_subscriptions(page_token=page_token, user_id=user_id, page_size=page_size, x_tableau_auth=x_tableau_auth, metric_id=metric_id)

Lists the subscriptions available on a server.

Lists the subscriptions available on a server. Only subscriptions a user has privileges to view will be visible.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_list_subscriptions_response import TableauPulseSubscriptionserviceV1ListSubscriptionsResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    page_token = 'page_token_example' # str | Specifies the page of items to be returned from a requested list. The value of `page_token` for the next page of returns is found in the `next_page_token` of the current response. If there are no further items to return, the value of `next_page_token` will be empty.  Example:  > `GET ...//subscriptions?pageToken={next_page_value}` Combining Path Parameters:  A page_token expression can be combined with other path parameters using an ampersand (&) as a separator, and is typically used along with a page number expression.   <a href='https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm' target='_blank'>Learn more about paginating the response</a>. (optional)
    user_id = 'user_id_example' # str |  (optional)
    page_size = 56 # int | Specifies the number of results in a paged response.   Example:   > `GET ...//subscriptions?pageSize=50`   Combining Path Parameters:  A page_size expression can be combined with other path parameters using an ampersand (&) as a separator, and is typically used along with a page number expression.   <a href='https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm' target='_blank'>Learn more about paginating the response</a>. (optional)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    metric_id = 'metric_id_example' # str |  (optional)

    try:
        # Lists the subscriptions available on a server.
        api_response = api_instance.pulse_subscription_service_list_subscriptions(page_token=page_token, user_id=user_id, page_size=page_size, x_tableau_auth=x_tableau_auth, metric_id=metric_id)
        print("The response of SubscriptionsApi->pulse_subscription_service_list_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_list_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_token** | **str**| Specifies the page of items to be returned from a requested list. The value of &#x60;page_token&#x60; for the next page of returns is found in the &#x60;next_page_token&#x60; of the current response. If there are no further items to return, the value of &#x60;next_page_token&#x60; will be empty.  Example:  &gt; &#x60;GET ...//subscriptions?pageToken&#x3D;{next_page_value}&#x60; Combining Path Parameters:  A page_token expression can be combined with other path parameters using an ampersand (&amp;) as a separator, and is typically used along with a page number expression.   &lt;a href&#x3D;&#39;https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Learn more about paginating the response&lt;/a&gt;. | [optional] 
 **user_id** | **str**|  | [optional] 
 **page_size** | **int**| Specifies the number of results in a paged response.   Example:   &gt; &#x60;GET ...//subscriptions?pageSize&#x3D;50&#x60;   Combining Path Parameters:  A page_size expression can be combined with other path parameters using an ampersand (&amp;) as a separator, and is typically used along with a page number expression.   &lt;a href&#x3D;&#39;https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_paging.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Learn more about paginating the response&lt;/a&gt;. | [optional] 
 **x_tableau_auth** | **str**|  | [optional] 
 **metric_id** | **str**|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1ListSubscriptionsResponse**](TableauPulseSubscriptionserviceV1ListSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.ListSubscriptionsResponse+json, application/json

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

# **pulse_subscription_service_update_subscription**
> TableauPulseSubscriptionserviceV1UpdateSubscriptionResponse pulse_subscription_service_update_subscription(id, x_tableau_auth=x_tableau_auth, tableau_pulse_subscriptionservice_v1_update_subscription_request=tableau_pulse_subscriptionservice_v1_update_subscription_request)

Updates a subscription.

Updates a subscription.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_update_subscription_request import TableauPulseSubscriptionserviceV1UpdateSubscriptionRequest
from openapi_client.models.tableau_pulse_subscriptionservice_v1_update_subscription_response import TableauPulseSubscriptionserviceV1UpdateSubscriptionResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    id = 'id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_pulse_subscriptionservice_v1_update_subscription_request = openapi_client.TableauPulseSubscriptionserviceV1UpdateSubscriptionRequest() # TableauPulseSubscriptionserviceV1UpdateSubscriptionRequest |  (optional)

    try:
        # Updates a subscription.
        api_response = api_instance.pulse_subscription_service_update_subscription(id, x_tableau_auth=x_tableau_auth, tableau_pulse_subscriptionservice_v1_update_subscription_request=tableau_pulse_subscriptionservice_v1_update_subscription_request)
        print("The response of SubscriptionsApi->pulse_subscription_service_update_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_update_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_pulse_subscriptionservice_v1_update_subscription_request** | [**TableauPulseSubscriptionserviceV1UpdateSubscriptionRequest**](TableauPulseSubscriptionserviceV1UpdateSubscriptionRequest.md)|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1UpdateSubscriptionResponse**](TableauPulseSubscriptionserviceV1UpdateSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.pulse.subscriptionservice.v1.UpdateSubscriptionRequest+json
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.UpdateSubscriptionResponse+json, application/json

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

# **pulse_subscription_service_update_user_digest_preferences**
> TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse pulse_subscription_service_update_user_digest_preferences(x_tableau_auth=x_tableau_auth, tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request=tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request)

Update user digest preferences

Updates the user's digest preferences for which delivery channels to receive notifications on, and at what cadence.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request import TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest
from openapi_client.models.tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_response import TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request = openapi_client.TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest() # TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest |  (optional)

    try:
        # Update user digest preferences
        api_response = api_instance.pulse_subscription_service_update_user_digest_preferences(x_tableau_auth=x_tableau_auth, tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request=tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request)
        print("The response of SubscriptionsApi->pulse_subscription_service_update_user_digest_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_update_user_digest_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_pulse_subscriptionservice_v1_update_user_digest_preferences_request** | [**TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest**](TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesRequest.md)|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse**](TableauPulseSubscriptionserviceV1UpdateUserDigestPreferencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.pulse.subscriptionservice.v1.UpdateUserDigestPreferencesRequest+json
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.UpdateUserDigestPreferencesResponse+json, application/json

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

# **pulse_subscription_service_update_user_preferences**
> TableauPulseSubscriptionserviceV1UpdateUserPreferencesResponse pulse_subscription_service_update_user_preferences(x_tableau_auth=x_tableau_auth, tableau_pulse_subscriptionservice_v1_update_user_preferences_request=tableau_pulse_subscriptionservice_v1_update_user_preferences_request)

Update user preferences

Updates the user's preferences for notifications channels and cadence, and for grouping and sorting followed metrics in REST responses and UI.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_subscriptionservice_v1_update_user_preferences_request import TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest
from openapi_client.models.tableau_pulse_subscriptionservice_v1_update_user_preferences_response import TableauPulseSubscriptionserviceV1UpdateUserPreferencesResponse
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
    api_instance = openapi_client.SubscriptionsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_pulse_subscriptionservice_v1_update_user_preferences_request = openapi_client.TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest() # TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest |  (optional)

    try:
        # Update user preferences
        api_response = api_instance.pulse_subscription_service_update_user_preferences(x_tableau_auth=x_tableau_auth, tableau_pulse_subscriptionservice_v1_update_user_preferences_request=tableau_pulse_subscriptionservice_v1_update_user_preferences_request)
        print("The response of SubscriptionsApi->pulse_subscription_service_update_user_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->pulse_subscription_service_update_user_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_pulse_subscriptionservice_v1_update_user_preferences_request** | [**TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest**](TableauPulseSubscriptionserviceV1UpdateUserPreferencesRequest.md)|  | [optional] 

### Return type

[**TableauPulseSubscriptionserviceV1UpdateUserPreferencesResponse**](TableauPulseSubscriptionserviceV1UpdateUserPreferencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.pulse.subscriptionservice.v1.UpdateUserPreferencesRequest+json
 - **Accept**: application/vnd.tableau.pulse.subscriptionservice.v1.UpdateUserPreferencesResponse+json, application/json

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

