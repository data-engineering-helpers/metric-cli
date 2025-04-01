# openapi_client.SettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_extensions_service_add_analytics_extensions_connection**](SettingsApi.md#analytics_extensions_service_add_analytics_extensions_connection) | **POST** /api/-/settings/site/extensions/analytics/connections | Add analytics extension connection to site
[**analytics_extensions_service_delete_analytics_extensions_connection**](SettingsApi.md#analytics_extensions_service_delete_analytics_extensions_connection) | **DELETE** /api/-/settings/site/extensions/analytics/connections/{connection_luid} | Delete analytics extension connection from site
[**analytics_extensions_service_delete_connection_from_workbook**](SettingsApi.md#analytics_extensions_service_delete_connection_from_workbook) | **DELETE** /api/-/settings/site/extensions/analytics/workbooks/{workbook_luid}/selected_connection | Remove current analytics extension connection for workbook
[**analytics_extensions_service_get_analytics_extensions_connection**](SettingsApi.md#analytics_extensions_service_get_analytics_extensions_connection) | **GET** /api/-/settings/site/extensions/analytics/connections/{connection_luid} | Get analytics extension details
[**analytics_extensions_service_get_analytics_extensions_connections**](SettingsApi.md#analytics_extensions_service_get_analytics_extensions_connections) | **GET** /api/-/settings/site/extensions/analytics/connections | List analytics extension connections on site
[**analytics_extensions_service_get_analytics_extensions_server_settings**](SettingsApi.md#analytics_extensions_service_get_analytics_extensions_server_settings) | **GET** /api/-/settings/server/extensions/analytics | Get enabled state of analytics extensions on server
[**analytics_extensions_service_get_analytics_extensions_site_settings**](SettingsApi.md#analytics_extensions_service_get_analytics_extensions_site_settings) | **GET** /api/-/settings/site/extensions/analytics | Get enabled state of analytics extensions on site
[**analytics_extensions_service_get_connection_options_for_workbook**](SettingsApi.md#analytics_extensions_service_get_connection_options_for_workbook) | **GET** /api/-/settings/site/extensions/analytics/workbooks/{workbook_luid}/connections | List analytics extension connections of workbook
[**analytics_extensions_service_get_selected_connection_for_workbook**](SettingsApi.md#analytics_extensions_service_get_selected_connection_for_workbook) | **GET** /api/-/settings/site/extensions/analytics/workbooks/{workbook_luid}/selected_connection | Get current analytics extension for workbook
[**analytics_extensions_service_update_analytics_extensions_connection**](SettingsApi.md#analytics_extensions_service_update_analytics_extensions_connection) | **PUT** /api/-/settings/site/extensions/analytics/connections/{connection_luid} | Update analytics extension connection of site
[**analytics_extensions_service_update_analytics_extensions_server_settings**](SettingsApi.md#analytics_extensions_service_update_analytics_extensions_server_settings) | **PUT** /api/-/settings/server/extensions/analytics | Enable/disable analytics extensions on server
[**analytics_extensions_service_update_analytics_extensions_site_settings**](SettingsApi.md#analytics_extensions_service_update_analytics_extensions_site_settings) | **PUT** /api/-/settings/site/extensions/analytics | Update enabled state of analytics extensions on site
[**analytics_extensions_service_update_workbook_with_connection**](SettingsApi.md#analytics_extensions_service_update_workbook_with_connection) | **PUT** /api/-/settings/site/extensions/analytics/workbooks/{workbook_luid}/selected_connection | Update analytics extension for workbook


# **analytics_extensions_service_add_analytics_extensions_connection**
> TableauAnalyticsextensionsV1ConnectionItem analytics_extensions_service_add_analytics_extensions_connection(x_tableau_auth=x_tableau_auth, tableau_analyticsextensions_v1_connection_item=tableau_analyticsextensions_v1_connection_item)

Add analytics extension connection to site

Adds an analytics extensions connection for an external service to a site. Permissions - This method can be called by site and server administrators.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_connection_item import TableauAnalyticsextensionsV1ConnectionItem
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
    api_instance = openapi_client.SettingsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_analyticsextensions_v1_connection_item = openapi_client.TableauAnalyticsextensionsV1ConnectionItem() # TableauAnalyticsextensionsV1ConnectionItem |  (optional)

    try:
        # Add analytics extension connection to site
        api_response = api_instance.analytics_extensions_service_add_analytics_extensions_connection(x_tableau_auth=x_tableau_auth, tableau_analyticsextensions_v1_connection_item=tableau_analyticsextensions_v1_connection_item)
        print("The response of SettingsApi->analytics_extensions_service_add_analytics_extensions_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_add_analytics_extensions_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_analyticsextensions_v1_connection_item** | [**TableauAnalyticsextensionsV1ConnectionItem**](TableauAnalyticsextensionsV1ConnectionItem.md)|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1ConnectionItem**](TableauAnalyticsextensionsV1ConnectionItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.analyticsextensions.v1.ConnectionItem+json
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.ConnectionItem+json, application/json

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

# **analytics_extensions_service_delete_analytics_extensions_connection**
> analytics_extensions_service_delete_analytics_extensions_connection(connection_luid, x_tableau_auth=x_tableau_auth)

Delete analytics extension connection from site

Deletes a specific analytics extension connection for an external service from a site. Permissions - This method can be called by site and server administrators.

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
    api_instance = openapi_client.SettingsApi(api_client)
    connection_luid = 'connection_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Delete analytics extension connection from site
        api_instance.analytics_extensions_service_delete_analytics_extensions_connection(connection_luid, x_tableau_auth=x_tableau_auth)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_delete_analytics_extensions_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_luid** | **str**|  | 
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

# **analytics_extensions_service_delete_connection_from_workbook**
> analytics_extensions_service_delete_connection_from_workbook(workbook_luid, x_tableau_auth=x_tableau_auth)

Remove current analytics extension connection for workbook

Remove the currently used analytics extension connection to an external service  from the specified workbook. The connection remains configured, and is available for further usage by the workbook. Permissions - This method can be called by users with authoring access to the workbook.

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
    api_instance = openapi_client.SettingsApi(api_client)
    workbook_luid = 'workbook_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Remove current analytics extension connection for workbook
        api_instance.analytics_extensions_service_delete_connection_from_workbook(workbook_luid, x_tableau_auth=x_tableau_auth)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_delete_connection_from_workbook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workbook_luid** | **str**|  | 
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

# **analytics_extensions_service_get_analytics_extensions_connection**
> TableauAnalyticsextensionsV1ConnectionItem analytics_extensions_service_get_analytics_extensions_connection(connection_luid, x_tableau_auth=x_tableau_auth)

Get analytics extension details

Get the details of a specified analytics extension connection to an external service. Permissions - This method can only be called by users with server or site administrator permissions.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_connection_item import TableauAnalyticsextensionsV1ConnectionItem
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
    api_instance = openapi_client.SettingsApi(api_client)
    connection_luid = 'connection_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get analytics extension details
        api_response = api_instance.analytics_extensions_service_get_analytics_extensions_connection(connection_luid, x_tableau_auth=x_tableau_auth)
        print("The response of SettingsApi->analytics_extensions_service_get_analytics_extensions_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_get_analytics_extensions_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1ConnectionItem**](TableauAnalyticsextensionsV1ConnectionItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.ConnectionItem+json, application/json

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

# **analytics_extensions_service_get_analytics_extensions_connections**
> TableauAnalyticsextensionsV1ConnectionList analytics_extensions_service_get_analytics_extensions_connections(x_tableau_auth=x_tableau_auth)

List analytics extension connections on site

Lists a site's analytics extension connections for external services. Permissions- This method can be called by site and server administrators.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_connection_list import TableauAnalyticsextensionsV1ConnectionList
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
    api_instance = openapi_client.SettingsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # List analytics extension connections on site
        api_response = api_instance.analytics_extensions_service_get_analytics_extensions_connections(x_tableau_auth=x_tableau_auth)
        print("The response of SettingsApi->analytics_extensions_service_get_analytics_extensions_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_get_analytics_extensions_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1ConnectionList**](TableauAnalyticsextensionsV1ConnectionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.ConnectionList+json, application/json

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

# **analytics_extensions_service_get_analytics_extensions_server_settings**
> TableauAnalyticsextensionsV1ServerSettings analytics_extensions_service_get_analytics_extensions_server_settings(x_tableau_auth=x_tableau_auth)

Get enabled state of analytics extensions on server

Gets the enabled/disabled state of analytics extensions on a server. Permissions - This method can only be called by server administrators.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_server_settings import TableauAnalyticsextensionsV1ServerSettings
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
    api_instance = openapi_client.SettingsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get enabled state of analytics extensions on server
        api_response = api_instance.analytics_extensions_service_get_analytics_extensions_server_settings(x_tableau_auth=x_tableau_auth)
        print("The response of SettingsApi->analytics_extensions_service_get_analytics_extensions_server_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_get_analytics_extensions_server_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1ServerSettings**](TableauAnalyticsextensionsV1ServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.ServerSettings+json, application/json

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

# **analytics_extensions_service_get_analytics_extensions_site_settings**
> TableauAnalyticsextensionsV1SiteSettings analytics_extensions_service_get_analytics_extensions_site_settings(x_tableau_auth=x_tableau_auth)

Get enabled state of analytics extensions on site

Gets the enabled/disabled state of analytics extensions on a site. Permissions - This method can be called by site and server administrators.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_site_settings import TableauAnalyticsextensionsV1SiteSettings
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
    api_instance = openapi_client.SettingsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get enabled state of analytics extensions on site
        api_response = api_instance.analytics_extensions_service_get_analytics_extensions_site_settings(x_tableau_auth=x_tableau_auth)
        print("The response of SettingsApi->analytics_extensions_service_get_analytics_extensions_site_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_get_analytics_extensions_site_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1SiteSettings**](TableauAnalyticsextensionsV1SiteSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.SiteSettings+json, application/json

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

# **analytics_extensions_service_get_connection_options_for_workbook**
> TableauAnalyticsextensionsV1ConnectionMetadataList analytics_extensions_service_get_connection_options_for_workbook(workbook_luid, x_tableau_auth=x_tableau_auth)

List analytics extension connections of workbook

Lists basic details of each analytics extension connection available for a specified workbook, including connection type and name. Permissions - This method can be called by users that have permissions to the specified workbook.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_connection_metadata_list import TableauAnalyticsextensionsV1ConnectionMetadataList
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
    api_instance = openapi_client.SettingsApi(api_client)
    workbook_luid = 'workbook_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # List analytics extension connections of workbook
        api_response = api_instance.analytics_extensions_service_get_connection_options_for_workbook(workbook_luid, x_tableau_auth=x_tableau_auth)
        print("The response of SettingsApi->analytics_extensions_service_get_connection_options_for_workbook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_get_connection_options_for_workbook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workbook_luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1ConnectionMetadataList**](TableauAnalyticsextensionsV1ConnectionMetadataList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.ConnectionMetadataList+json, application/json

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

# **analytics_extensions_service_get_selected_connection_for_workbook**
> TableauAnalyticsextensionsV1ConnectionMetadata analytics_extensions_service_get_selected_connection_for_workbook(workbook_luid, x_tableau_auth=x_tableau_auth)

Get current analytics extension for workbook

Gets basic details, including connection type and name, of the analytics extension connection to an external service that the specified workbook is currently using. Permissions - This method can be called by users with authoring access to the workbook.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_connection_metadata import TableauAnalyticsextensionsV1ConnectionMetadata
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
    api_instance = openapi_client.SettingsApi(api_client)
    workbook_luid = 'workbook_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get current analytics extension for workbook
        api_response = api_instance.analytics_extensions_service_get_selected_connection_for_workbook(workbook_luid, x_tableau_auth=x_tableau_auth)
        print("The response of SettingsApi->analytics_extensions_service_get_selected_connection_for_workbook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_get_selected_connection_for_workbook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workbook_luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1ConnectionMetadata**](TableauAnalyticsextensionsV1ConnectionMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.ConnectionMetadata+json, application/json

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

# **analytics_extensions_service_update_analytics_extensions_connection**
> TableauAnalyticsextensionsV1ConnectionItem analytics_extensions_service_update_analytics_extensions_connection(connection_luid, x_tableau_auth=x_tableau_auth, tableau_analyticsextensions_v1_connection_item=tableau_analyticsextensions_v1_connection_item)

Update analytics extension connection of site

Updates the details of specified analytics extension connection for an external service to a site. Permissions - This method can be called by site and server administrators.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_connection_item import TableauAnalyticsextensionsV1ConnectionItem
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
    api_instance = openapi_client.SettingsApi(api_client)
    connection_luid = 'connection_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_analyticsextensions_v1_connection_item = openapi_client.TableauAnalyticsextensionsV1ConnectionItem() # TableauAnalyticsextensionsV1ConnectionItem |  (optional)

    try:
        # Update analytics extension connection of site
        api_response = api_instance.analytics_extensions_service_update_analytics_extensions_connection(connection_luid, x_tableau_auth=x_tableau_auth, tableau_analyticsextensions_v1_connection_item=tableau_analyticsextensions_v1_connection_item)
        print("The response of SettingsApi->analytics_extensions_service_update_analytics_extensions_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_update_analytics_extensions_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_analyticsextensions_v1_connection_item** | [**TableauAnalyticsextensionsV1ConnectionItem**](TableauAnalyticsextensionsV1ConnectionItem.md)|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1ConnectionItem**](TableauAnalyticsextensionsV1ConnectionItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.analyticsextensions.v1.ConnectionItem+json
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.ConnectionItem+json, application/json

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

# **analytics_extensions_service_update_analytics_extensions_server_settings**
> TableauAnalyticsextensionsV1ServerSettings analytics_extensions_service_update_analytics_extensions_server_settings(x_tableau_auth=x_tableau_auth, tableau_analyticsextensions_v1_server_settings=tableau_analyticsextensions_v1_server_settings)

Enable/disable analytics extensions on server

Enables or disables analytics extensions on a server. Permissions - This method can only be called by server administrators.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_server_settings import TableauAnalyticsextensionsV1ServerSettings
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
    api_instance = openapi_client.SettingsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_analyticsextensions_v1_server_settings = openapi_client.TableauAnalyticsextensionsV1ServerSettings() # TableauAnalyticsextensionsV1ServerSettings |  (optional)

    try:
        # Enable/disable analytics extensions on server
        api_response = api_instance.analytics_extensions_service_update_analytics_extensions_server_settings(x_tableau_auth=x_tableau_auth, tableau_analyticsextensions_v1_server_settings=tableau_analyticsextensions_v1_server_settings)
        print("The response of SettingsApi->analytics_extensions_service_update_analytics_extensions_server_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_update_analytics_extensions_server_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_analyticsextensions_v1_server_settings** | [**TableauAnalyticsextensionsV1ServerSettings**](TableauAnalyticsextensionsV1ServerSettings.md)|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1ServerSettings**](TableauAnalyticsextensionsV1ServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.analyticsextensions.v1.ServerSettings+json
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.ServerSettings+json, application/json

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

# **analytics_extensions_service_update_analytics_extensions_site_settings**
> TableauAnalyticsextensionsV1SiteSettings analytics_extensions_service_update_analytics_extensions_site_settings(x_tableau_auth=x_tableau_auth, tableau_analyticsextensions_v1_site_settings=tableau_analyticsextensions_v1_site_settings)

Update enabled state of analytics extensions on site

Enables or disables analytics extensions on a site. Permissions - This method can be called by site and server administrators.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_site_settings import TableauAnalyticsextensionsV1SiteSettings
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
    api_instance = openapi_client.SettingsApi(api_client)
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_analyticsextensions_v1_site_settings = openapi_client.TableauAnalyticsextensionsV1SiteSettings() # TableauAnalyticsextensionsV1SiteSettings |  (optional)

    try:
        # Update enabled state of analytics extensions on site
        api_response = api_instance.analytics_extensions_service_update_analytics_extensions_site_settings(x_tableau_auth=x_tableau_auth, tableau_analyticsextensions_v1_site_settings=tableau_analyticsextensions_v1_site_settings)
        print("The response of SettingsApi->analytics_extensions_service_update_analytics_extensions_site_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_update_analytics_extensions_site_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_analyticsextensions_v1_site_settings** | [**TableauAnalyticsextensionsV1SiteSettings**](TableauAnalyticsextensionsV1SiteSettings.md)|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1SiteSettings**](TableauAnalyticsextensionsV1SiteSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.analyticsextensions.v1.SiteSettings+json
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.SiteSettings+json, application/json

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

# **analytics_extensions_service_update_workbook_with_connection**
> TableauAnalyticsextensionsV1ConnectionMapping analytics_extensions_service_update_workbook_with_connection(workbook_luid, x_tableau_auth=x_tableau_auth, tableau_analyticsextensions_v1_connection_mapping=tableau_analyticsextensions_v1_connection_mapping)

Update analytics extension for workbook

Updates the analytics extension connection to external service currently used by a workbook. Permissions - This method can be called by users that have permissions to the specified workbook.

### Example


```python
import openapi_client
from openapi_client.models.tableau_analyticsextensions_v1_connection_mapping import TableauAnalyticsextensionsV1ConnectionMapping
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
    api_instance = openapi_client.SettingsApi(api_client)
    workbook_luid = 'workbook_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_analyticsextensions_v1_connection_mapping = openapi_client.TableauAnalyticsextensionsV1ConnectionMapping() # TableauAnalyticsextensionsV1ConnectionMapping |  (optional)

    try:
        # Update analytics extension for workbook
        api_response = api_instance.analytics_extensions_service_update_workbook_with_connection(workbook_luid, x_tableau_auth=x_tableau_auth, tableau_analyticsextensions_v1_connection_mapping=tableau_analyticsextensions_v1_connection_mapping)
        print("The response of SettingsApi->analytics_extensions_service_update_workbook_with_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->analytics_extensions_service_update_workbook_with_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workbook_luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_analyticsextensions_v1_connection_mapping** | [**TableauAnalyticsextensionsV1ConnectionMapping**](TableauAnalyticsextensionsV1ConnectionMapping.md)|  | [optional] 

### Return type

[**TableauAnalyticsextensionsV1ConnectionMapping**](TableauAnalyticsextensionsV1ConnectionMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.analyticsextensions.v1.ConnectionMapping+json
 - **Accept**: application/vnd.tableau.analyticsextensions.v1.ConnectionMapping+json, application/json

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

