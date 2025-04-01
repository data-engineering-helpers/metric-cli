# TableauAuthnV1ListAuthConfigurationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[TableauAuthnV1AuthConfiguration]**](TableauAuthnV1AuthConfiguration.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_list_auth_configurations_response import TableauAuthnV1ListAuthConfigurationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1ListAuthConfigurationsResponse from a JSON string
tableau_authn_v1_list_auth_configurations_response_instance = TableauAuthnV1ListAuthConfigurationsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1ListAuthConfigurationsResponse.to_json())

# convert the object into a dict
tableau_authn_v1_list_auth_configurations_response_dict = tableau_authn_v1_list_auth_configurations_response_instance.to_dict()
# create an instance of TableauAuthnV1ListAuthConfigurationsResponse from a dict
tableau_authn_v1_list_auth_configurations_response_from_dict = TableauAuthnV1ListAuthConfigurationsResponse.from_dict(tableau_authn_v1_list_auth_configurations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


