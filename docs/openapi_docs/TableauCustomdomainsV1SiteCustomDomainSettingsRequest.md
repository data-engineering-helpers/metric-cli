# TableauCustomdomainsV1SiteCustomDomainSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_luid** | **str** | The LUID of the Tableau site associated with the custom  domain. | [optional] 
**custom_domain** | **str** | The custom domain associated with the Tableau site. | [optional] 
**status** | **str** | The provisioning status of the custom domain. | [optional] 
**tls_certificate** | **str** | The TLS certificate for the custom domain, including the CA certs. | [optional] 
**tls_certificate_private_key** | **str** | The private key corresponding to the TLS certificate. | [optional] 

## Example

```python
from openapi_client.models.tableau_customdomains_v1_site_custom_domain_settings_request import TableauCustomdomainsV1SiteCustomDomainSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauCustomdomainsV1SiteCustomDomainSettingsRequest from a JSON string
tableau_customdomains_v1_site_custom_domain_settings_request_instance = TableauCustomdomainsV1SiteCustomDomainSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(TableauCustomdomainsV1SiteCustomDomainSettingsRequest.to_json())

# convert the object into a dict
tableau_customdomains_v1_site_custom_domain_settings_request_dict = tableau_customdomains_v1_site_custom_domain_settings_request_instance.to_dict()
# create an instance of TableauCustomdomainsV1SiteCustomDomainSettingsRequest from a dict
tableau_customdomains_v1_site_custom_domain_settings_request_from_dict = TableauCustomdomainsV1SiteCustomDomainSettingsRequest.from_dict(tableau_customdomains_v1_site_custom_domain_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


