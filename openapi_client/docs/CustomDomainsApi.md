# openapi_client.CustomDomainsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_domains_service_create_site_custom_domain_settings**](CustomDomainsApi.md#custom_domains_service_create_site_custom_domain_settings) | **POST** /api/-/customdomains/settings/site/{site_luid} | Create custom domain settings
[**custom_domains_service_delete_site_custom_domain_settings**](CustomDomainsApi.md#custom_domains_service_delete_site_custom_domain_settings) | **DELETE** /api/-/customdomains/settings/site/{site_luid} | Delete custom domain settings
[**custom_domains_service_get_site_custom_domain**](CustomDomainsApi.md#custom_domains_service_get_site_custom_domain) | **GET** /api/-/customdomains/site/{site_luid} | Get Custom Domain Name
[**custom_domains_service_get_site_custom_domain_settings**](CustomDomainsApi.md#custom_domains_service_get_site_custom_domain_settings) | **GET** /api/-/customdomains/settings/site/{site_luid} | Get custom domain settings
[**custom_domains_service_update_site_custom_domain_settings**](CustomDomainsApi.md#custom_domains_service_update_site_custom_domain_settings) | **PUT** /api/-/customdomains/settings/site/{site_luid} | Update custom domain settings


# **custom_domains_service_create_site_custom_domain_settings**
> TableauCustomdomainsV1SiteCustomDomainSettingsResponse custom_domains_service_create_site_custom_domain_settings(site_luid, x_tableau_auth=x_tableau_auth, tableau_customdomains_v1_site_custom_domain_settings_request=tableau_customdomains_v1_site_custom_domain_settings_request)

Create custom domain settings

<a name='create_custom_domain_settings'></a>Starts the process of custom domain setup for a Tableau site. <br/>For more information, see [Setup Steps to Enable a Custom Domain](#setup_steps_to_enable_a_custom_domain).   > **Version:** Available in API 3.21 (Tableau Cloud October 2023) and later. Not available for Tableau Server. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Only users  with administrator permissions can create a custom domain for a site. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Cloud](https://help.tableau.com/current/online/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_customdomains_v1_site_custom_domain_settings_request import TableauCustomdomainsV1SiteCustomDomainSettingsRequest
from openapi_client.models.tableau_customdomains_v1_site_custom_domain_settings_response import TableauCustomdomainsV1SiteCustomDomainSettingsResponse
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
    api_instance = openapi_client.CustomDomainsApi(api_client)
    site_luid = 'site_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_customdomains_v1_site_custom_domain_settings_request = openapi_client.TableauCustomdomainsV1SiteCustomDomainSettingsRequest() # TableauCustomdomainsV1SiteCustomDomainSettingsRequest |  (optional)

    try:
        # Create custom domain settings
        api_response = api_instance.custom_domains_service_create_site_custom_domain_settings(site_luid, x_tableau_auth=x_tableau_auth, tableau_customdomains_v1_site_custom_domain_settings_request=tableau_customdomains_v1_site_custom_domain_settings_request)
        print("The response of CustomDomainsApi->custom_domains_service_create_site_custom_domain_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDomainsApi->custom_domains_service_create_site_custom_domain_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_customdomains_v1_site_custom_domain_settings_request** | [**TableauCustomdomainsV1SiteCustomDomainSettingsRequest**](TableauCustomdomainsV1SiteCustomDomainSettingsRequest.md)|  | [optional] 

### Return type

[**TableauCustomdomainsV1SiteCustomDomainSettingsResponse**](TableauCustomdomainsV1SiteCustomDomainSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.customdomains.v1.SiteCustomDomainSettingsRequest+json
 - **Accept**: application/vnd.tableau.customdomains.v1.SiteCustomDomainSettingsResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful. |  -  |
**400** | The request was malformed. |  -  |
**401** | User could not be authenticated. Credentials were missing or invalid. |  -  |
**500** | An unknown error occured. |  -  |
**404** | The requested resource could not be found. |  -  |
**503** | Tableau service was unavailable. Retry at a later time. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_domains_service_delete_site_custom_domain_settings**
> TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse custom_domains_service_delete_site_custom_domain_settings(site_luid, x_tableau_auth=x_tableau_auth)

Delete custom domain settings

Deletes the custom domain setup for a Tableau site.   > **Version:** Available in API 3.21 (Tableau Cloud October 2023) and later. Not available for Tableau Server. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Only users  with administrator permissions can view a site's custom domain settings. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Cloud](https://help.tableau.com/current/online/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_customdomains_v1_delete_site_custom_domain_settings_response import TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse
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
    api_instance = openapi_client.CustomDomainsApi(api_client)
    site_luid = 'site_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Delete custom domain settings
        api_response = api_instance.custom_domains_service_delete_site_custom_domain_settings(site_luid, x_tableau_auth=x_tableau_auth)
        print("The response of CustomDomainsApi->custom_domains_service_delete_site_custom_domain_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDomainsApi->custom_domains_service_delete_site_custom_domain_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse**](TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.customdomains.v1.DeleteSiteCustomDomainSettingsResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | The request was malformed. |  -  |
**401** | User could not be authenticated. Credentials were missing or invalid. |  -  |
**500** | An unknown error occured. |  -  |
**204** | Successful. |  -  |
**404** | The requested resource could not be found. |  -  |
**503** | Tableau service was unavailable. Retry at a later time. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_domains_service_get_site_custom_domain**
> TableauCustomdomainsV1GetSiteCustomDomainResponse custom_domains_service_get_site_custom_domain(site_luid, x_tableau_auth=x_tableau_auth)

Get Custom Domain Name

Gets the custom domain for a Tableau site, if one is provisioned. For more information about how, see [Using Custom Domains](https://help.tableau.com/current/online/en-us/custom_domain.htm).   > **Version:** Available in API 3.21 (Tableau Cloud October 2023) and later. Not available for Tableau Server. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Can be called by any user that is a member of the site associated with the custom domain. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Cloud](https://help.tableau.com/current/online/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_customdomains_v1_get_site_custom_domain_response import TableauCustomdomainsV1GetSiteCustomDomainResponse
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
    api_instance = openapi_client.CustomDomainsApi(api_client)
    site_luid = 'site_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get Custom Domain Name
        api_response = api_instance.custom_domains_service_get_site_custom_domain(site_luid, x_tableau_auth=x_tableau_auth)
        print("The response of CustomDomainsApi->custom_domains_service_get_site_custom_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDomainsApi->custom_domains_service_get_site_custom_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauCustomdomainsV1GetSiteCustomDomainResponse**](TableauCustomdomainsV1GetSiteCustomDomainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.customdomains.v1.GetSiteCustomDomainResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful. |  -  |
**400** | The request was malformed. |  -  |
**401** | User could not be authenticated. Credentials were missing or invalid. |  -  |
**500** | An unknown error occured. |  -  |
**404** | The requested resource could not be found. |  -  |
**503** | Tableau service was unavailable. Retry at a later time. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_domains_service_get_site_custom_domain_settings**
> TableauCustomdomainsV1SiteCustomDomainSettingsResponse custom_domains_service_get_site_custom_domain_settings(site_luid, x_tableau_auth=x_tableau_auth)

Get custom domain settings

Gets the custom domain settings for a Tableau site.   > **Version:** Available in API 3.21 (Tableau Cloud October 2023) and later. Not available for Tableau Server. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Only users  with administrator permissions can view a site's custom domain settings. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Cloud](https://help.tableau.com/current/online/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_customdomains_v1_site_custom_domain_settings_response import TableauCustomdomainsV1SiteCustomDomainSettingsResponse
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
    api_instance = openapi_client.CustomDomainsApi(api_client)
    site_luid = 'site_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)

    try:
        # Get custom domain settings
        api_response = api_instance.custom_domains_service_get_site_custom_domain_settings(site_luid, x_tableau_auth=x_tableau_auth)
        print("The response of CustomDomainsApi->custom_domains_service_get_site_custom_domain_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDomainsApi->custom_domains_service_get_site_custom_domain_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 

### Return type

[**TableauCustomdomainsV1SiteCustomDomainSettingsResponse**](TableauCustomdomainsV1SiteCustomDomainSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tableau.customdomains.v1.SiteCustomDomainSettingsResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful. |  -  |
**400** | The request was malformed. |  -  |
**401** | User could not be authenticated. Credentials were missing or invalid. |  -  |
**500** | An unknown error occured. |  -  |
**404** | The requested resource could not be found. |  -  |
**503** | Tableau service was unavailable. Retry at a later time. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_domains_service_update_site_custom_domain_settings**
> TableauCustomdomainsV1SiteCustomDomainSettingsResponse custom_domains_service_update_site_custom_domain_settings(site_luid, x_tableau_auth=x_tableau_auth, tableau_customdomains_v1_site_custom_domain_settings_request=tableau_customdomains_v1_site_custom_domain_settings_request)

Update custom domain settings

<a name='update_custom_domain_settings'></a>Updates the custom domain setup for a Tableau site. <br/>For more information, see [Setup Steps to Enable a Custom Domain](#setup_steps_to_enable_a_custom_domain).   > **Version:** Available in API 3.21 (Tableau Cloud October 2023) and later. Not available for Tableau Server. *[Versioning Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm)*   > **Permissions:** Only users  with administrator permissions can update a site's custom domain settings. *[Permissions Overview](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_permissions.htm)*   > **License:** No additional license required.   > **Access Scope:** Not available.<br/>*Access Scopes Overview: [Cloud](https://help.tableau.com/current/online/en-us/connected_apps_scopes.htm)*

### Example


```python
import openapi_client
from openapi_client.models.tableau_customdomains_v1_site_custom_domain_settings_request import TableauCustomdomainsV1SiteCustomDomainSettingsRequest
from openapi_client.models.tableau_customdomains_v1_site_custom_domain_settings_response import TableauCustomdomainsV1SiteCustomDomainSettingsResponse
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
    api_instance = openapi_client.CustomDomainsApi(api_client)
    site_luid = 'site_luid_example' # str | 
    x_tableau_auth = 'x_tableau_auth_example' # str |  (optional)
    tableau_customdomains_v1_site_custom_domain_settings_request = openapi_client.TableauCustomdomainsV1SiteCustomDomainSettingsRequest() # TableauCustomdomainsV1SiteCustomDomainSettingsRequest |  (optional)

    try:
        # Update custom domain settings
        api_response = api_instance.custom_domains_service_update_site_custom_domain_settings(site_luid, x_tableau_auth=x_tableau_auth, tableau_customdomains_v1_site_custom_domain_settings_request=tableau_customdomains_v1_site_custom_domain_settings_request)
        print("The response of CustomDomainsApi->custom_domains_service_update_site_custom_domain_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDomainsApi->custom_domains_service_update_site_custom_domain_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_luid** | **str**|  | 
 **x_tableau_auth** | **str**|  | [optional] 
 **tableau_customdomains_v1_site_custom_domain_settings_request** | [**TableauCustomdomainsV1SiteCustomDomainSettingsRequest**](TableauCustomdomainsV1SiteCustomDomainSettingsRequest.md)|  | [optional] 

### Return type

[**TableauCustomdomainsV1SiteCustomDomainSettingsResponse**](TableauCustomdomainsV1SiteCustomDomainSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.tableau.customdomains.v1.SiteCustomDomainSettingsRequest+json
 - **Accept**: application/vnd.tableau.customdomains.v1.SiteCustomDomainSettingsResponse+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful. |  -  |
**400** | The request was malformed. |  -  |
**401** | User could not be authenticated. Credentials were missing or invalid. |  -  |
**500** | An unknown error occured. |  -  |
**404** | The requested resource could not be found. |  -  |
**503** | Tableau service was unavailable. Retry at a later time. |  -  |
**0** | Successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

