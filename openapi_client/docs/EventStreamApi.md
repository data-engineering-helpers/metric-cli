# openapi_client.EventStreamApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_service_publish**](EventStreamApi.md#event_service_publish) | **POST** /api/-/eventservice/events | Publish a Pulse event.
[**event_service_publish_ui_event**](EventStreamApi.md#event_service_publish_ui_event) | **POST** /api/-/eventservice/publishUIEvent | Publish a UI event.


# **event_service_publish**
> TableauEventserviceV1PublishResponse event_service_publish(x_tableau_auth=x_tableau_auth, tableau_eventservice_v1_publish_request=tableau_eventservice_v1_publish_request)

Publish a Pulse event.

Publish a new event on the Pulse Event Stream.

### Example


```python
import openapi_client
from openapi_client.models.tableau_eventservice_v1_publish_request import TableauEventserviceV1PublishRequest
from openapi_client.models.tableau_eventservice_v1_publish_response import TableauEventserviceV1PublishResponse
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
    api_instance = openapi_client.EventStreamApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_eventservice_v1_publish_request = openapi_client.TableauEventserviceV1PublishRequest() # TableauEventserviceV1PublishRequest |  (optional)

    try:
        # Publish a Pulse event.
        api_response = api_instance.event_service_publish(x_tableau_auth=x_tableau_auth, tableau_eventservice_v1_publish_request=tableau_eventservice_v1_publish_request)
        print("The response of EventStreamApi->event_service_publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventStreamApi->event_service_publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_eventservice_v1_publish_request** | [**TableauEventserviceV1PublishRequest**](TableauEventserviceV1PublishRequest.md)|  | [optional] 

### Return type

[**TableauEventserviceV1PublishResponse**](TableauEventserviceV1PublishResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.eventservice.v1.PublishRequest+json
 - **Accept**: application/vnd.tableau.eventservice.v1.PublishResponse+json, application/json

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

# **event_service_publish_ui_event**
> TableauEventserviceV1PublishUIEventResponse event_service_publish_ui_event(x_tableau_auth=x_tableau_auth, tableau_eventservice_v1_publish_ui_event_request=tableau_eventservice_v1_publish_ui_event_request)

Publish a UI event.

Publish a UI event on the Pulse Event Stream.

### Example


```python
import openapi_client
from openapi_client.models.tableau_eventservice_v1_publish_ui_event_request import TableauEventserviceV1PublishUIEventRequest
from openapi_client.models.tableau_eventservice_v1_publish_ui_event_response import TableauEventserviceV1PublishUIEventResponse
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
    api_instance = openapi_client.EventStreamApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_eventservice_v1_publish_ui_event_request = openapi_client.TableauEventserviceV1PublishUIEventRequest() # TableauEventserviceV1PublishUIEventRequest |  (optional)

    try:
        # Publish a UI event.
        api_response = api_instance.event_service_publish_ui_event(x_tableau_auth=x_tableau_auth, tableau_eventservice_v1_publish_ui_event_request=tableau_eventservice_v1_publish_ui_event_request)
        print("The response of EventStreamApi->event_service_publish_ui_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventStreamApi->event_service_publish_ui_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_eventservice_v1_publish_ui_event_request** | [**TableauEventserviceV1PublishUIEventRequest**](TableauEventserviceV1PublishUIEventRequest.md)|  | [optional] 

### Return type

[**TableauEventserviceV1PublishUIEventResponse**](TableauEventserviceV1PublishUIEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.eventservice.v1.PublishUIEventRequest+json
 - **Accept**: application/vnd.tableau.eventservice.v1.PublishUIEventResponse+json, application/json

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

