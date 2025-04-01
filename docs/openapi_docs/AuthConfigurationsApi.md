# openapi_client.AuthConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authn_service_delete_auth_configuration**](AuthConfigurationsApi.md#authn_service_delete_auth_configuration) | **DELETE** /api/-/authn-service/auth-configurations/{id} | Delete Authentication Configuration
[**authn_service_list_auth_configurations**](AuthConfigurationsApi.md#authn_service_list_auth_configurations) | **GET** /api/-/authn-service/auth-configurations/ | List Authentication Configurations
[**authn_service_register_auth_configuration**](AuthConfigurationsApi.md#authn_service_register_auth_configuration) | **POST** /api/-/authn-service/auth-configurations/ | Create Authentication Configuration
[**authn_service_update_auth_configuration**](AuthConfigurationsApi.md#authn_service_update_auth_configuration) | **PUT** /api/-/authn-service/auth-configurations/{id} | Update Authentication Configuration


# **authn_service_delete_auth_configuration**
> authn_service_delete_auth_configuration(id, x_tableau_auth=x_tableau_auth)

Delete Authentication Configuration

Delete an authentication instance.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

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
    api_instance = openapi_client.AuthConfigurationsApi(api_client)
    id = 56 # int | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Delete Authentication Configuration
        api_instance.authn_service_delete_auth_configuration(id, x_tableau_auth=x_tableau_auth)
    except Exception as e:
        print("Exception when calling AuthConfigurationsApi->authn_service_delete_auth_configuration: %s\n" % e)
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

# **authn_service_list_auth_configurations**
> TableauAuthnV1ListAuthConfigurationsResponse authn_service_list_auth_configurations(x_tableau_auth=x_tableau_auth)

List Authentication Configurations

List information about all authentication instances.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_authn_v1_list_auth_configurations_response import TableauAuthnV1ListAuthConfigurationsResponse
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
    api_instance = openapi_client.AuthConfigurationsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # List Authentication Configurations
        api_response = api_instance.authn_service_list_auth_configurations(x_tableau_auth=x_tableau_auth)
        print("The response of AuthConfigurationsApi->authn_service_list_auth_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthConfigurationsApi->authn_service_list_auth_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauAuthnV1ListAuthConfigurationsResponse**](TableauAuthnV1ListAuthConfigurationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.authn.v1.ListAuthConfigurationsResponse+json, application/json

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

# **authn_service_register_auth_configuration**
> TableauAuthnV1RegisterAuthConfigurationResponse authn_service_register_auth_configuration(x_tableau_auth=x_tableau_auth, tableau_authn_v1_register_auth_configuration_request=tableau_authn_v1_register_auth_configuration_request)

Create Authentication Configuration

Create an instance of OpenID Connect (OIDC) authentication.   For more information, see [Step 3: Set up authentication](https://help.tableau.com/current/server/en-us/identity_pools_manage.htm#step3) in the Tableau Server Help.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_authn_v1_register_auth_configuration_request import TableauAuthnV1RegisterAuthConfigurationRequest
from openapi_client.models.tableau_authn_v1_register_auth_configuration_response import TableauAuthnV1RegisterAuthConfigurationResponse
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
    api_instance = openapi_client.AuthConfigurationsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_authn_v1_register_auth_configuration_request = openapi_client.TableauAuthnV1RegisterAuthConfigurationRequest() # TableauAuthnV1RegisterAuthConfigurationRequest |  (optional)

    try:
        # Create Authentication Configuration
        api_response = api_instance.authn_service_register_auth_configuration(x_tableau_auth=x_tableau_auth, tableau_authn_v1_register_auth_configuration_request=tableau_authn_v1_register_auth_configuration_request)
        print("The response of AuthConfigurationsApi->authn_service_register_auth_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthConfigurationsApi->authn_service_register_auth_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_authn_v1_register_auth_configuration_request** | [**TableauAuthnV1RegisterAuthConfigurationRequest**](TableauAuthnV1RegisterAuthConfigurationRequest.md)|  | [optional] 

### Return type

[**TableauAuthnV1RegisterAuthConfigurationResponse**](TableauAuthnV1RegisterAuthConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.authn.v1.RegisterAuthConfigurationRequest+json
 - **Accept**: application/vnd.tableau.authn.v1.RegisterAuthConfigurationResponse+json, application/json

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

# **authn_service_update_auth_configuration**
> TableauAuthnV1UpdateAuthConfigurationResponse authn_service_update_auth_configuration(id, x_tableau_auth=x_tableau_auth, tableau_authn_v1_update_auth_configuration_request=tableau_authn_v1_update_auth_configuration_request)

Update Authentication Configuration

Update an authentication instance.   **Note:** The request body must specify all the required and desired parameters, not just the parameters you want to update.   > **Version:** Available in API 3.19 (Tableau Server 2023.1) and later. Not available in Tableau Cloud. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can only be called by users with server administrator permissions. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Server-Windows](https://help.tableau.com/current/server/en-us/connected_apps_scopes.htm) | [Server-Linux](https://help.tableau.com/current/server-linux/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_authn_v1_update_auth_configuration_request import TableauAuthnV1UpdateAuthConfigurationRequest
from openapi_client.models.tableau_authn_v1_update_auth_configuration_response import TableauAuthnV1UpdateAuthConfigurationResponse
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
    api_instance = openapi_client.AuthConfigurationsApi(api_client)
    id = 56 # int | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_authn_v1_update_auth_configuration_request = openapi_client.TableauAuthnV1UpdateAuthConfigurationRequest() # TableauAuthnV1UpdateAuthConfigurationRequest |  (optional)

    try:
        # Update Authentication Configuration
        api_response = api_instance.authn_service_update_auth_configuration(id, x_tableau_auth=x_tableau_auth, tableau_authn_v1_update_auth_configuration_request=tableau_authn_v1_update_auth_configuration_request)
        print("The response of AuthConfigurationsApi->authn_service_update_auth_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthConfigurationsApi->authn_service_update_auth_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_authn_v1_update_auth_configuration_request** | [**TableauAuthnV1UpdateAuthConfigurationRequest**](TableauAuthnV1UpdateAuthConfigurationRequest.md)|  | [optional] 

### Return type

[**TableauAuthnV1UpdateAuthConfigurationResponse**](TableauAuthnV1UpdateAuthConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.authn.v1.UpdateAuthConfigurationRequest+json
 - **Accept**: application/vnd.tableau.authn.v1.UpdateAuthConfigurationResponse+json, application/json

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

