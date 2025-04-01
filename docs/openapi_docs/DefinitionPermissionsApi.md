# openapi_client.DefinitionPermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permission_service_add_definition_permissions**](DefinitionPermissionsApi.md#permission_service_add_definition_permissions) | **POST** /api/-/pulse/definitions/{definition_id}/permissions:add | Add definition permission records to the definition specified by the id.
[**permission_service_delete_definition_permissions**](DefinitionPermissionsApi.md#permission_service_delete_definition_permissions) | **POST** /api/-/pulse/definitions/{definition_id}/permissions:delete | Delete definition permission records from the definition specified by the id.
[**permission_service_get_definition_permissions**](DefinitionPermissionsApi.md#permission_service_get_definition_permissions) | **GET** /api/-/pulse/definitions/{definition_id}/permissions | Get definition permission records for the definition specified by the id.
[**permission_service_has_effective_permissions**](DefinitionPermissionsApi.md#permission_service_has_effective_permissions) | **GET** /api/-/pulse/definitions/{definition_id}/permissions:hasEffectivePermissions | Based on the site role and other rules get the effective permissions of the current user


# **permission_service_add_definition_permissions**
> TableauPermissionserviceV1AddDefinitionPermissionsResponse permission_service_add_definition_permissions(definition_id, x_tableau_auth=x_tableau_auth, tableau_permissionservice_v1_add_definition_permissions_request=tableau_permissionservice_v1_add_definition_permissions_request)

Add definition permission records to the definition specified by the id.

Add definition permission records on the definition

### Example


```python
import openapi_client
from openapi_client.models.tableau_permissionservice_v1_add_definition_permissions_request import TableauPermissionserviceV1AddDefinitionPermissionsRequest
from openapi_client.models.tableau_permissionservice_v1_add_definition_permissions_response import TableauPermissionserviceV1AddDefinitionPermissionsResponse
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
    api_instance = openapi_client.DefinitionPermissionsApi(api_client)
    definition_id = 'definition_id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_permissionservice_v1_add_definition_permissions_request = openapi_client.TableauPermissionserviceV1AddDefinitionPermissionsRequest() # TableauPermissionserviceV1AddDefinitionPermissionsRequest |  (optional)

    try:
        # Add definition permission records to the definition specified by the id.
        api_response = api_instance.permission_service_add_definition_permissions(definition_id, x_tableau_auth=x_tableau_auth, tableau_permissionservice_v1_add_definition_permissions_request=tableau_permissionservice_v1_add_definition_permissions_request)
        print("The response of DefinitionPermissionsApi->permission_service_add_definition_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefinitionPermissionsApi->permission_service_add_definition_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_permissionservice_v1_add_definition_permissions_request** | [**TableauPermissionserviceV1AddDefinitionPermissionsRequest**](TableauPermissionserviceV1AddDefinitionPermissionsRequest.md)|  | [optional] 

### Return type

[**TableauPermissionserviceV1AddDefinitionPermissionsResponse**](TableauPermissionserviceV1AddDefinitionPermissionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.permissionservice.v1.AddDefinitionPermissionsRequest+json
 - **Accept**: application/vnd.tableau.permissionservice.v1.AddDefinitionPermissionsResponse+json, application/json

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

# **permission_service_delete_definition_permissions**
> TableauPermissionserviceV1DeleteDefinitionPermissionsResponse permission_service_delete_definition_permissions(definition_id, x_tableau_auth=x_tableau_auth, tableau_permissionservice_v1_delete_definition_permissions_request=tableau_permissionservice_v1_delete_definition_permissions_request)

Delete definition permission records from the definition specified by the id.

Delete definition permission records on the definition

### Example


```python
import openapi_client
from openapi_client.models.tableau_permissionservice_v1_delete_definition_permissions_request import TableauPermissionserviceV1DeleteDefinitionPermissionsRequest
from openapi_client.models.tableau_permissionservice_v1_delete_definition_permissions_response import TableauPermissionserviceV1DeleteDefinitionPermissionsResponse
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
    api_instance = openapi_client.DefinitionPermissionsApi(api_client)
    definition_id = 'definition_id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_permissionservice_v1_delete_definition_permissions_request = openapi_client.TableauPermissionserviceV1DeleteDefinitionPermissionsRequest() # TableauPermissionserviceV1DeleteDefinitionPermissionsRequest |  (optional)

    try:
        # Delete definition permission records from the definition specified by the id.
        api_response = api_instance.permission_service_delete_definition_permissions(definition_id, x_tableau_auth=x_tableau_auth, tableau_permissionservice_v1_delete_definition_permissions_request=tableau_permissionservice_v1_delete_definition_permissions_request)
        print("The response of DefinitionPermissionsApi->permission_service_delete_definition_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefinitionPermissionsApi->permission_service_delete_definition_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_permissionservice_v1_delete_definition_permissions_request** | [**TableauPermissionserviceV1DeleteDefinitionPermissionsRequest**](TableauPermissionserviceV1DeleteDefinitionPermissionsRequest.md)|  | [optional] 

### Return type

[**TableauPermissionserviceV1DeleteDefinitionPermissionsResponse**](TableauPermissionserviceV1DeleteDefinitionPermissionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.permissionservice.v1.DeleteDefinitionPermissionsRequest+json
 - **Accept**: application/vnd.tableau.permissionservice.v1.DeleteDefinitionPermissionsResponse+json, application/json

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

# **permission_service_get_definition_permissions**
> TableauPermissionserviceV1GetDefinitionPermissionsResponse permission_service_get_definition_permissions(definition_id, x_tableau_auth=x_tableau_auth)

Get definition permission records for the definition specified by the id.

Get all definition permission records on the definition

### Example


```python
import openapi_client
from openapi_client.models.tableau_permissionservice_v1_get_definition_permissions_response import TableauPermissionserviceV1GetDefinitionPermissionsResponse
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
    api_instance = openapi_client.DefinitionPermissionsApi(api_client)
    definition_id = 'definition_id_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get definition permission records for the definition specified by the id.
        api_response = api_instance.permission_service_get_definition_permissions(definition_id, x_tableau_auth=x_tableau_auth)
        print("The response of DefinitionPermissionsApi->permission_service_get_definition_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefinitionPermissionsApi->permission_service_get_definition_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_id** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauPermissionserviceV1GetDefinitionPermissionsResponse**](TableauPermissionserviceV1GetDefinitionPermissionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.permissionservice.v1.GetDefinitionPermissionsResponse+json, application/json

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

# **permission_service_has_effective_permissions**
> TableauPermissionserviceV1HasEffectivePermissionsResponse permission_service_has_effective_permissions(definition_id, permissions=permissions, x_tableau_auth=x_tableau_auth)

Based on the site role and other rules get the effective permissions of the current user

Get effective permissions of the current user

### Example


```python
import openapi_client
from openapi_client.models.tableau_permissionservice_v1_has_effective_permissions_response import TableauPermissionserviceV1HasEffectivePermissionsResponse
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
    api_instance = openapi_client.DefinitionPermissionsApi(api_client)
    definition_id = 'definition_id_example' # str | 
    permissions = 'permissions_example' # str |  (optional)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Based on the site role and other rules get the effective permissions of the current user
        api_response = api_instance.permission_service_has_effective_permissions(definition_id, permissions=permissions, x_tableau_auth=x_tableau_auth)
        print("The response of DefinitionPermissionsApi->permission_service_has_effective_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefinitionPermissionsApi->permission_service_has_effective_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definition_id** | **str**|  | 
 **permissions** | **str**|  | [optional] 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauPermissionserviceV1HasEffectivePermissionsResponse**](TableauPermissionserviceV1HasEffectivePermissionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.permissionservice.v1.HasEffectivePermissionsResponse+json, application/json

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

