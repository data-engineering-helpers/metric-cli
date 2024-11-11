# openapi_client.AskDataLensesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lens_service_create_lens**](AskDataLensesApi.md#lens_service_create_lens) | **POST** /api/-/askdata/lenses | Create a lens
[**lens_service_delete_lens**](AskDataLensesApi.md#lens_service_delete_lens) | **DELETE** /api/-/askdata/lenses/{lens_id} | Delete a lens
[**lens_service_get_lens**](AskDataLensesApi.md#lens_service_get_lens) | **GET** /api/-/askdata/lenses/{lens_id} | Get ask data lens details
[**lens_service_import_lens**](AskDataLensesApi.md#lens_service_import_lens) | **POST** /api/-/askdata/lenses/import | Import a lens
[**lens_service_list_lenses**](AskDataLensesApi.md#lens_service_list_lenses) | **GET** /api/-/askdata/lenses | Get ask data lens list


# **lens_service_create_lens**
> TableauNlpLensPublicrestV1CreateLensResponse lens_service_create_lens(x_tableau_auth=x_tableau_auth, tableau_nlp_lens_publicrest_v1_create_lens_request=tableau_nlp_lens_publicrest_v1_create_lens_request)

Create a lens

Create an ask data lens. Permissions- This can be invoked by a user who has permission to create lens.

### Example


```python
import openapi_client
from openapi_client.models.tableau_nlp_lens_publicrest_v1_create_lens_request import TableauNlpLensPublicrestV1CreateLensRequest
from openapi_client.models.tableau_nlp_lens_publicrest_v1_create_lens_response import TableauNlpLensPublicrestV1CreateLensResponse
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
    api_instance = openapi_client.AskDataLensesApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_nlp_lens_publicrest_v1_create_lens_request = openapi_client.TableauNlpLensPublicrestV1CreateLensRequest() # TableauNlpLensPublicrestV1CreateLensRequest |  (optional)

    try:
        # Create a lens
        api_response = api_instance.lens_service_create_lens(x_tableau_auth=x_tableau_auth, tableau_nlp_lens_publicrest_v1_create_lens_request=tableau_nlp_lens_publicrest_v1_create_lens_request)
        print("The response of AskDataLensesApi->lens_service_create_lens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskDataLensesApi->lens_service_create_lens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_nlp_lens_publicrest_v1_create_lens_request** | [**TableauNlpLensPublicrestV1CreateLensRequest**](TableauNlpLensPublicrestV1CreateLensRequest.md)|  | [optional] 

### Return type

[**TableauNlpLensPublicrestV1CreateLensResponse**](TableauNlpLensPublicrestV1CreateLensResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.nlp.lens.publicrest.v1.CreateLensRequest+json
 - **Accept**: application/vnd.tableau.nlp.lens.publicrest.v1.CreateLensResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful. |  -  |
**400** | invalid datasource id |  -  |
**401** | Unable to authenticate user. Credentials are missing or invalid. |  -  |
**500** | exception from permission service |  -  |
**404** | datasource not found |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lens_service_delete_lens**
> lens_service_delete_lens(lens_id, x_tableau_auth=x_tableau_auth)

Delete a lens

Delete an Ask Data lens. Permissions- This can be invoked by a user who has permission to delete a lens.

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
    api_instance = openapi_client.AskDataLensesApi(api_client)
    lens_id = 'lens_id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Delete a lens
        api_instance.lens_service_delete_lens(lens_id, x_tableau_auth=x_tableau_auth)
    except Exception as e:
        print("Exception when calling AskDataLensesApi->lens_service_delete_lens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lens_id** | **str**|  | 
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

# **lens_service_get_lens**
> TableauNlpLensPublicrestV1GetLensResponse lens_service_get_lens(lens_id, x_tableau_auth=x_tableau_auth)

Get ask data lens details

Get the details of a lens. Permissions - This method can be called by users who have read access to the lens.

### Example


```python
import openapi_client
from openapi_client.models.tableau_nlp_lens_publicrest_v1_get_lens_response import TableauNlpLensPublicrestV1GetLensResponse
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
    api_instance = openapi_client.AskDataLensesApi(api_client)
    lens_id = 'lens_id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get ask data lens details
        api_response = api_instance.lens_service_get_lens(lens_id, x_tableau_auth=x_tableau_auth)
        print("The response of AskDataLensesApi->lens_service_get_lens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskDataLensesApi->lens_service_get_lens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lens_id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauNlpLensPublicrestV1GetLensResponse**](TableauNlpLensPublicrestV1GetLensResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.nlp.lens.publicrest.v1.GetLensResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful. |  -  |
**400** | invalid lens id (luid) |  -  |
**401** | Unable to authenticate user. Credentials are missing or invalid. |  -  |
**500** | internal database exception |  -  |
**404** | datasource not found |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lens_service_import_lens**
> TableauNlpLensPublicrestV1ImportLensResponse lens_service_import_lens(x_tableau_auth=x_tableau_auth, tableau_nlp_lens_publicrest_v1_import_lens_request=tableau_nlp_lens_publicrest_v1_import_lens_request)

Import a lens

This API lets you import a lens in to the site. Useful when you want to publish a lens across projects, sites etc. The input to this API is a lens that already exist in a server. You can get the details of the lens using the getLens method and submit to this method. During an import, you can use transformations to apply on the exported lens. Permissions - This method can only be called by server administrators or site administrators.

### Example


```python
import openapi_client
from openapi_client.models.tableau_nlp_lens_publicrest_v1_import_lens_request import TableauNlpLensPublicrestV1ImportLensRequest
from openapi_client.models.tableau_nlp_lens_publicrest_v1_import_lens_response import TableauNlpLensPublicrestV1ImportLensResponse
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
    api_instance = openapi_client.AskDataLensesApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_nlp_lens_publicrest_v1_import_lens_request = openapi_client.TableauNlpLensPublicrestV1ImportLensRequest() # TableauNlpLensPublicrestV1ImportLensRequest |  (optional)

    try:
        # Import a lens
        api_response = api_instance.lens_service_import_lens(x_tableau_auth=x_tableau_auth, tableau_nlp_lens_publicrest_v1_import_lens_request=tableau_nlp_lens_publicrest_v1_import_lens_request)
        print("The response of AskDataLensesApi->lens_service_import_lens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskDataLensesApi->lens_service_import_lens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_nlp_lens_publicrest_v1_import_lens_request** | [**TableauNlpLensPublicrestV1ImportLensRequest**](TableauNlpLensPublicrestV1ImportLensRequest.md)|  | [optional] 

### Return type

[**TableauNlpLensPublicrestV1ImportLensResponse**](TableauNlpLensPublicrestV1ImportLensResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.nlp.lens.publicrest.v1.ImportLensRequest+json
 - **Accept**: application/vnd.tableau.nlp.lens.publicrest.v1.ImportLensResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful. |  -  |
**400** | invalid datasource id |  -  |
**401** | only system admin or site admin can use this method |  -  |
**500** | exception from permission service |  -  |
**404** | datasource not found |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lens_service_list_lenses**
> TableauNlpLensPublicrestV1ListLensesResponse lens_service_list_lenses(x_tableau_auth=x_tableau_auth)

Get ask data lens list

Returns a list of lenses in a site. Permissions - This method can be called by any user and they will see the lenses to which they have access to.

### Example


```python
import openapi_client
from openapi_client.models.tableau_nlp_lens_publicrest_v1_list_lenses_response import TableauNlpLensPublicrestV1ListLensesResponse
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
    api_instance = openapi_client.AskDataLensesApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get ask data lens list
        api_response = api_instance.lens_service_list_lenses(x_tableau_auth=x_tableau_auth)
        print("The response of AskDataLensesApi->lens_service_list_lenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskDataLensesApi->lens_service_list_lenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauNlpLensPublicrestV1ListLensesResponse**](TableauNlpLensPublicrestV1ListLensesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.nlp.lens.publicrest.v1.ListLensesResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful. |  -  |
**400** | Invalid Request. The requested was incorrect. |  -  |
**401** | Unable to authenticate user. Credentials are missing or invalid. |  -  |
**500** | failed to get list of lenses |  -  |
**404** | Bad Request. The requested resource could not be found. |  -  |
**503** | Service unavailable. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

