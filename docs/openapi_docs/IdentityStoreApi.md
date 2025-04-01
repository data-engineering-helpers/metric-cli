# openapi_client.IdentityStoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authn_service_delete_identity_store_tag**](IdentityStoreApi.md#authn_service_delete_identity_store_tag) | **DELETE** /api/-/authn-service/identity-stores/{id} | Delete Identity Store
[**authn_service_list_identity_stores_tag**](IdentityStoreApi.md#authn_service_list_identity_stores_tag) | **GET** /api/-/authn-service/identity-stores/ | List Identity Stores
[**authn_service_register_identity_store_tag**](IdentityStoreApi.md#authn_service_register_identity_store_tag) | **POST** /api/-/authn-service/identity-stores/ | Configure Identity Store


# **authn_service_delete_identity_store_tag**
> authn_service_delete_identity_store_tag(id, x_tableau_auth=x_tableau_auth)

Delete Identity Store

Delete an identity store.   **Note:** You cannot delete the identity store you configured during Tableau Server setup.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

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
    api_instance = openapi_client.IdentityStoreApi(api_client)
    id = 56 # int | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Delete Identity Store
        api_instance.authn_service_delete_identity_store_tag(id, x_tableau_auth=x_tableau_auth)
    except Exception as e:
        print("Exception when calling IdentityStoreApi->authn_service_delete_identity_store_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
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

# **authn_service_list_identity_stores_tag**
> TableauAuthnV1ListIdentityStoresResponse authn_service_list_identity_stores_tag(x_tableau_auth=x_tableau_auth)

List Identity Stores

List information about all identity store instances used to provision users.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_authn_v1_list_identity_stores_response import TableauAuthnV1ListIdentityStoresResponse
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
    api_instance = openapi_client.IdentityStoreApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # List Identity Stores
        api_response = api_instance.authn_service_list_identity_stores_tag(x_tableau_auth=x_tableau_auth)
        print("The response of IdentityStoreApi->authn_service_list_identity_stores_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityStoreApi->authn_service_list_identity_stores_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauAuthnV1ListIdentityStoresResponse**](TableauAuthnV1ListIdentityStoresResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.authn.v1.ListIdentityStoresResponse+json, application/json

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

# **authn_service_register_identity_store_tag**
> TableauAuthnV1RegisterIdentityStoreResponse authn_service_register_identity_store_tag(x_tableau_auth=x_tableau_auth, tableau_authn_v1_register_identity_store_request=tableau_authn_v1_register_identity_store_request)

Configure Identity Store

Configure a new local identity store to provision users.   For more information, see [Step 2: Set up an identity store](https://help.tableau.com/current/server/en-us/identity_pools_manage.htm#step2) in the Tableau Server Help.   **Note:** This identity store is in addition to the identity store you configured during Tableau Server setup.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_authn_v1_register_identity_store_request import TableauAuthnV1RegisterIdentityStoreRequest
from openapi_client.models.tableau_authn_v1_register_identity_store_response import TableauAuthnV1RegisterIdentityStoreResponse
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
    api_instance = openapi_client.IdentityStoreApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_authn_v1_register_identity_store_request = openapi_client.TableauAuthnV1RegisterIdentityStoreRequest() # TableauAuthnV1RegisterIdentityStoreRequest |  (optional)

    try:
        # Configure Identity Store
        api_response = api_instance.authn_service_register_identity_store_tag(x_tableau_auth=x_tableau_auth, tableau_authn_v1_register_identity_store_request=tableau_authn_v1_register_identity_store_request)
        print("The response of IdentityStoreApi->authn_service_register_identity_store_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityStoreApi->authn_service_register_identity_store_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_authn_v1_register_identity_store_request** | [**TableauAuthnV1RegisterIdentityStoreRequest**](TableauAuthnV1RegisterIdentityStoreRequest.md)|  | [optional] 

### Return type

[**TableauAuthnV1RegisterIdentityStoreResponse**](TableauAuthnV1RegisterIdentityStoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.authn.v1.RegisterIdentityStoreRequest+json
 - **Accept**: application/vnd.tableau.authn.v1.RegisterIdentityStoreResponse+json, application/json

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

