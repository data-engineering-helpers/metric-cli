# TableauCustomdomainsV1SiteCustomDomainSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_luid** | **str** | The LUID of the Tableau site associated with the custom  domain. | [optional] 
**custom_domain** | **str** | The custom domain associated with the Tableau site. | [optional] 
**intermediate_domain** | **str** | The Tableau intermediate domain associated with the site. | [optional] 
**status** | **str** | The provisioning status of the custom domain. | [optional] 
**request_initiation_date** | **str** | The timestamp of when the create request was received. The format is like: &lt;code&gt;2024-06-05T08:15:09Z&lt;/code&gt;. | [optional] 
**tls_certificate_uploaded_date** | **str** | The timestamp of when the TLS certificate was uploaded. The format is like: &lt;code&gt;2024-06-05T08:15:09Z&lt;/code&gt;. | [optional] 
**tls_certificate_expiry_date** | **str** | The TLS certificate expiry date. The format is like: &lt;code&gt;2024-06-05T08:15:09Z&lt;/code&gt;. | [optional] 
**certificate_update_in_progress** | **bool** | Indicates whether or not a certificate update is in progress. | [optional] 
**last_error** | **str** | Latest error which happened during certificate provisioning. | [optional] 

## Example

```python
from openapi_client.models.tableau_customdomains_v1_site_custom_domain_settings_response import TableauCustomdomainsV1SiteCustomDomainSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauCustomdomainsV1SiteCustomDomainSettingsResponse from a JSON string
tableau_customdomains_v1_site_custom_domain_settings_response_instance = TableauCustomdomainsV1SiteCustomDomainSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauCustomdomainsV1SiteCustomDomainSettingsResponse.to_json())

# convert the object into a dict
tableau_customdomains_v1_site_custom_domain_settings_response_dict = tableau_customdomains_v1_site_custom_domain_settings_response_instance.to_dict()
# create an instance of TableauCustomdomainsV1SiteCustomDomainSettingsResponse from a dict
tableau_customdomains_v1_site_custom_domain_settings_response_from_dict = TableauCustomdomainsV1SiteCustomDomainSettingsResponse.from_dict(tableau_customdomains_v1_site_custom_domain_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


