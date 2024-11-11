# openapi_client.IdentityPoolApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authn_service_delete_identity_pool**](IdentityPoolApi.md#authn_service_delete_identity_pool) | **DELETE** /api/-/authn-service/identity-pools/{uuid} | Delete Identity Pool
[**authn_service_find_identity_pool_by_uuid**](IdentityPoolApi.md#authn_service_find_identity_pool_by_uuid) | **GET** /api/-/authn-service/identity-pools/{uuid} | Get Identity Pool
[**authn_service_list_identity_pools**](IdentityPoolApi.md#authn_service_list_identity_pools) | **GET** /api/-/authn-service/identity-pools/ | List Identity Pools
[**authn_service_register_identity_pool**](IdentityPoolApi.md#authn_service_register_identity_pool) | **POST** /api/-/authn-service/identity-pools/ | Create Identity Pool
[**authn_service_update_identity_pool**](IdentityPoolApi.md#authn_service_update_identity_pool) | **PUT** /api/-/authn-service/identity-pools/{uuid} | Update Identity Pool


# **authn_service_delete_identity_pool**
> authn_service_delete_identity_pool(uuid, x_tableau_auth=x_tableau_auth)

Delete Identity Pool

Delete an identity pool.   **Note:** In Tableau Server, move users to another identity pool before deleting an identity pool. Users will no longer be able to sign in to Tableau Server unless they are a member of an identity pool.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

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
    api_instance = openapi_client.IdentityPoolApi(api_client)
    uuid = 'uuid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Delete Identity Pool
        api_instance.authn_service_delete_identity_pool(uuid, x_tableau_auth=x_tableau_auth)
    except Exception as e:
        print("Exception when calling IdentityPoolApi->authn_service_delete_identity_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
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

# **authn_service_find_identity_pool_by_uuid**
> TableauAuthnV1FindIdentityPoolByUuidResponse authn_service_find_identity_pool_by_uuid(uuid, x_tableau_auth=x_tableau_auth)

Get Identity Pool

Get information about an identity pool.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_authn_v1_find_identity_pool_by_uuid_response import TableauAuthnV1FindIdentityPoolByUuidResponse
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
    api_instance = openapi_client.IdentityPoolApi(api_client)
    uuid = 'uuid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get Identity Pool
        api_response = api_instance.authn_service_find_identity_pool_by_uuid(uuid, x_tableau_auth=x_tableau_auth)
        print("The response of IdentityPoolApi->authn_service_find_identity_pool_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityPoolApi->authn_service_find_identity_pool_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauAuthnV1FindIdentityPoolByUuidResponse**](TableauAuthnV1FindIdentityPoolByUuidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.authn.v1.FindIdentityPoolByUuidResponse+json, application/json

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

# **authn_service_list_identity_pools**
> TableauAuthnV1ListIdentityPoolsResponse authn_service_list_identity_pools()

List Identity Pools

List all identity pools.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_authn_v1_list_identity_pools_response import TableauAuthnV1ListIdentityPoolsResponse
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
    api_instance = openapi_client.IdentityPoolApi(api_client)

    try:
        # List Identity Pools
        api_response = api_instance.authn_service_list_identity_pools()
        print("The response of IdentityPoolApi->authn_service_list_identity_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityPoolApi->authn_service_list_identity_pools: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TableauAuthnV1ListIdentityPoolsResponse**](TableauAuthnV1ListIdentityPoolsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.authn.v1.ListIdentityPoolsResponse+json, application/json

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

# **authn_service_register_identity_pool**
> TableauAuthnV1RegisterIdentityPoolResponse authn_service_register_identity_pool(x_tableau_auth=x_tableau_auth, tableau_authn_v1_register_identity_pool_request=tableau_authn_v1_register_identity_pool_request)

Create Identity Pool

Create an identity pool.   For more information, see [Step 4: Create an identity pool](https://help.tableau.com/current/server/en-us/identity_pools_manage.htm#step4) in the Tableau Server Help.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_authn_v1_register_identity_pool_request import TableauAuthnV1RegisterIdentityPoolRequest
from openapi_client.models.tableau_authn_v1_register_identity_pool_response import TableauAuthnV1RegisterIdentityPoolResponse
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
    api_instance = openapi_client.IdentityPoolApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_authn_v1_register_identity_pool_request = openapi_client.TableauAuthnV1RegisterIdentityPoolRequest() # TableauAuthnV1RegisterIdentityPoolRequest |  (optional)

    try:
        # Create Identity Pool
        api_response = api_instance.authn_service_register_identity_pool(x_tableau_auth=x_tableau_auth, tableau_authn_v1_register_identity_pool_request=tableau_authn_v1_register_identity_pool_request)
        print("The response of IdentityPoolApi->authn_service_register_identity_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityPoolApi->authn_service_register_identity_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_authn_v1_register_identity_pool_request** | [**TableauAuthnV1RegisterIdentityPoolRequest**](TableauAuthnV1RegisterIdentityPoolRequest.md)|  | [optional] 

### Return type

[**TableauAuthnV1RegisterIdentityPoolResponse**](TableauAuthnV1RegisterIdentityPoolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.authn.v1.RegisterIdentityPoolRequest+json
 - **Accept**: application/vnd.tableau.authn.v1.RegisterIdentityPoolResponse+json, application/json

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

# **authn_service_update_identity_pool**
> TableauAuthnV1UpdateIdentityPoolResponse authn_service_update_identity_pool(uuid, x_tableau_auth=x_tableau_auth, tableau_authn_v1_update_identity_pool_request=tableau_authn_v1_update_identity_pool_request)

Update Identity Pool

Update information about an identity pool.   > **Note:** The request body must specify all the required and desired parameters, not just the parameters you want to update.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_authn_v1_update_identity_pool_request import TableauAuthnV1UpdateIdentityPoolRequest
from openapi_client.models.tableau_authn_v1_update_identity_pool_response import TableauAuthnV1UpdateIdentityPoolResponse
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
    api_instance = openapi_client.IdentityPoolApi(api_client)
    uuid = 'uuid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_authn_v1_update_identity_pool_request = openapi_client.TableauAuthnV1UpdateIdentityPoolRequest() # TableauAuthnV1UpdateIdentityPoolRequest |  (optional)

    try:
        # Update Identity Pool
        api_response = api_instance.authn_service_update_identity_pool(uuid, x_tableau_auth=x_tableau_auth, tableau_authn_v1_update_identity_pool_request=tableau_authn_v1_update_identity_pool_request)
        print("The response of IdentityPoolApi->authn_service_update_identity_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityPoolApi->authn_service_update_identity_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_authn_v1_update_identity_pool_request** | [**TableauAuthnV1UpdateIdentityPoolRequest**](TableauAuthnV1UpdateIdentityPoolRequest.md)|  | [optional] 

### Return type

[**TableauAuthnV1UpdateIdentityPoolResponse**](TableauAuthnV1UpdateIdentityPoolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.authn.v1.UpdateIdentityPoolRequest+json
 - **Accept**: application/vnd.tableau.authn.v1.UpdateIdentityPoolResponse+json, application/json

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

