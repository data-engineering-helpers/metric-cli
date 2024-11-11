# TableauCustomdomainsV1GetSiteCustomDomainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_luid** | **str** | The LUID of the Tableau site associated with the custom  domain. | [optional] 
**custom_domain** | **str** | The custom domain associated with the Tableau site. | [optional] 

## Example

```python
from openapi_client.models.tableau_customdomains_v1_get_site_custom_domain_response import TableauCustomdomainsV1GetSiteCustomDomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauCustomdomainsV1GetSiteCustomDomainResponse from a JSON string
tableau_customdomains_v1_get_site_custom_domain_response_instance = TableauCustomdomainsV1GetSiteCustomDomainResponse.from_json(json)
# print the JSON string representation of the object
print(TableauCustomdomainsV1GetSiteCustomDomainResponse.to_json())

# convert the object into a dict
tableau_customdomains_v1_get_site_custom_domain_response_dict = tableau_customdomains_v1_get_site_custom_domain_response_instance.to_dict()
# create an instance of TableauCustomdomainsV1GetSiteCustomDomainResponse from a dict
tableau_customdomains_v1_get_site_custom_domain_response_from_dict = TableauCustomdomainsV1GetSiteCustomDomainResponse.from_dict(tableau_customdomains_v1_get_site_custom_domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


