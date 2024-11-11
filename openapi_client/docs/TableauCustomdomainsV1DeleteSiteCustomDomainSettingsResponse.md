# TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_luid** | **str** | The LUID of the Tableau site associated with the custom  domain. | [optional] 

## Example

```python
from openapi_client.models.tableau_customdomains_v1_delete_site_custom_domain_settings_response import TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse from a JSON string
tableau_customdomains_v1_delete_site_custom_domain_settings_response_instance = TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse.to_json())

# convert the object into a dict
tableau_customdomains_v1_delete_site_custom_domain_settings_response_dict = tableau_customdomains_v1_delete_site_custom_domain_settings_response_instance.to_dict()
# create an instance of TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse from a dict
tableau_customdomains_v1_delete_site_custom_domain_settings_response_from_dict = TableauCustomdomainsV1DeleteSiteCustomDomainSettingsResponse.from_dict(tableau_customdomains_v1_delete_site_custom_domain_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


