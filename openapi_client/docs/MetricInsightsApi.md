# openapi_client.MetricInsightsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pulse_insights_service_generate_insight_bundle_ban**](MetricInsightsApi.md#pulse_insights_service_generate_insight_bundle_ban) | **POST** /api/-/pulse/insights/ban | Generates a BAN insight bundle.
[**pulse_insights_service_generate_insight_bundle_detail**](MetricInsightsApi.md#pulse_insights_service_generate_insight_bundle_detail) | **POST** /api/-/pulse/insights/detail | Generates a detail insight bundle.
[**pulse_insights_service_generate_insight_bundle_springboard**](MetricInsightsApi.md#pulse_insights_service_generate_insight_bundle_springboard) | **POST** /api/-/pulse/insights/springboard | Generates a springboard insight bundle.


# **pulse_insights_service_generate_insight_bundle_ban**
> TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse pulse_insights_service_generate_insight_bundle_ban(x_tableau_auth=x_tableau_auth, tableau_pulse_insightsservice_v1_generate_insight_bundle_ban_request=tableau_pulse_insightsservice_v1_generate_insight_bundle_ban_request)

Generates a BAN insight bundle.

Generates a BAN insight bundle.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_insightsservice_v1_generate_insight_bundle_ban_request import TableauPulseInsightsserviceV1GenerateInsightBundleBANRequest
from openapi_client.models.tableau_pulse_insightsservice_v1_generate_insight_bundle_ban_response import TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse
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
    api_instance = openapi_client.MetricInsightsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_pulse_insightsservice_v1_generate_insight_bundle_ban_request = openapi_client.TableauPulseInsightsserviceV1GenerateInsightBundleBANRequest() # TableauPulseInsightsserviceV1GenerateInsightBundleBANRequest |  (optional)

    try:
        # Generates a BAN insight bundle.
        api_response = api_instance.pulse_insights_service_generate_insight_bundle_ban(x_tableau_auth=x_tableau_auth, tableau_pulse_insightsservice_v1_generate_insight_bundle_ban_request=tableau_pulse_insightsservice_v1_generate_insight_bundle_ban_request)
        print("The response of MetricInsightsApi->pulse_insights_service_generate_insight_bundle_ban:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricInsightsApi->pulse_insights_service_generate_insight_bundle_ban: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_pulse_insightsservice_v1_generate_insight_bundle_ban_request** | [**TableauPulseInsightsserviceV1GenerateInsightBundleBANRequest**](TableauPulseInsightsserviceV1GenerateInsightBundleBANRequest.md)|  | [optional] 

### Return type

[**TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse**](TableauPulseInsightsserviceV1GenerateInsightBundleBANResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.pulse.insightsservice.v1.GenerateInsightBundleBANRequest+json
 - **Accept**: application/vnd.tableau.pulse.insightsservice.v1.GenerateInsightBundleBANResponse+json, application/json

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

# **pulse_insights_service_generate_insight_bundle_detail**
> TableauPulseInsightsserviceV1GenerateInsightBundleDetailResponse pulse_insights_service_generate_insight_bundle_detail(x_tableau_auth=x_tableau_auth, tableau_pulse_insightsservice_v1_generate_insight_bundle_detail_request=tableau_pulse_insightsservice_v1_generate_insight_bundle_detail_request)

Generates a detail insight bundle.

Generates a detail insight bundle.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_insightsservice_v1_generate_insight_bundle_detail_request import TableauPulseInsightsserviceV1GenerateInsightBundleDetailRequest
from openapi_client.models.tableau_pulse_insightsservice_v1_generate_insight_bundle_detail_response import TableauPulseInsightsserviceV1GenerateInsightBundleDetailResponse
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
    api_instance = openapi_client.MetricInsightsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_pulse_insightsservice_v1_generate_insight_bundle_detail_request = openapi_client.TableauPulseInsightsserviceV1GenerateInsightBundleDetailRequest() # TableauPulseInsightsserviceV1GenerateInsightBundleDetailRequest |  (optional)

    try:
        # Generates a detail insight bundle.
        api_response = api_instance.pulse_insights_service_generate_insight_bundle_detail(x_tableau_auth=x_tableau_auth, tableau_pulse_insightsservice_v1_generate_insight_bundle_detail_request=tableau_pulse_insightsservice_v1_generate_insight_bundle_detail_request)
        print("The response of MetricInsightsApi->pulse_insights_service_generate_insight_bundle_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricInsightsApi->pulse_insights_service_generate_insight_bundle_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_pulse_insightsservice_v1_generate_insight_bundle_detail_request** | [**TableauPulseInsightsserviceV1GenerateInsightBundleDetailRequest**](TableauPulseInsightsserviceV1GenerateInsightBundleDetailRequest.md)|  | [optional] 

### Return type

[**TableauPulseInsightsserviceV1GenerateInsightBundleDetailResponse**](TableauPulseInsightsserviceV1GenerateInsightBundleDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.pulse.insightsservice.v1.GenerateInsightBundleDetailRequest+json
 - **Accept**: application/vnd.tableau.pulse.insightsservice.v1.GenerateInsightBundleDetailResponse+json, application/json

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

# **pulse_insights_service_generate_insight_bundle_springboard**
> TableauPulseInsightsserviceV1GenerateInsightBundleSpringboardResponse pulse_insights_service_generate_insight_bundle_springboard(x_tableau_auth=x_tableau_auth, tableau_pulse_insightsservice_v1_generate_insight_bundle_springboard_request=tableau_pulse_insightsservice_v1_generate_insight_bundle_springboard_request)

Generates a springboard insight bundle.

Generates a springboard insight bundle.

### Example


```python
import openapi_client
from openapi_client.models.tableau_pulse_insightsservice_v1_generate_insight_bundle_springboard_request import TableauPulseInsightsserviceV1GenerateInsightBundleSpringboardRequest
from openapi_client.models.tableau_pulse_insightsservice_v1_generate_insight_bundle_springboard_response import TableauPulseInsightsserviceV1GenerateInsightBundleSpringboardResponse
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
    api_instance = openapi_client.MetricInsightsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_pulse_insightsservice_v1_generate_insight_bundle_springboard_request = openapi_client.TableauPulseInsightsserviceV1GenerateInsightBundleSpringboardRequest() # TableauPulseInsightsserviceV1GenerateInsightBundleSpringboardRequest |  (optional)

    try:
        # Generates a springboard insight bundle.
        api_response = api_instance.pulse_insights_service_generate_insight_bundle_springboard(x_tableau_auth=x_tableau_auth, tableau_pulse_insightsservice_v1_generate_insight_bundle_springboard_request=tableau_pulse_insightsservice_v1_generate_insight_bundle_springboard_request)
        print("The response of MetricInsightsApi->pulse_insights_service_generate_insight_bundle_springboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricInsightsApi->pulse_insights_service_generate_insight_bundle_springboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_pulse_insightsservice_v1_generate_insight_bundle_springboard_request** | [**TableauPulseInsightsserviceV1GenerateInsightBundleSpringboardRequest**](TableauPulseInsightsserviceV1GenerateInsightBundleSpringboardRequest.md)|  | [optional] 

### Return type

[**TableauPulseInsightsserviceV1GenerateInsightBundleSpringboardResponse**](TableauPulseInsightsserviceV1GenerateInsightBundleSpringboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.pulse.insightsservice.v1.GenerateInsightBundleSpringboardRequest+json
 - **Accept**: application/vnd.tableau.pulse.insightsservice.v1.GenerateInsightBundleSpringboardResponse+json, application/json

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

