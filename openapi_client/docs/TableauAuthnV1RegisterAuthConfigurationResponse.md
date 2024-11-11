# TableauAuthnV1RegisterAuthConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_configuration** | [**TableauAuthnV1AuthConfiguration**](TableauAuthnV1AuthConfiguration.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_register_auth_configuration_response import TableauAuthnV1RegisterAuthConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1RegisterAuthConfigurationResponse from a JSON string
tableau_authn_v1_register_auth_configuration_response_instance = TableauAuthnV1RegisterAuthConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1RegisterAuthConfigurationResponse.to_json())

# convert the object into a dict
tableau_authn_v1_register_auth_configuration_response_dict = tableau_authn_v1_register_auth_configuration_response_instance.to_dict()
# create an instance of TableauAuthnV1RegisterAuthConfigurationResponse from a dict
tableau_authn_v1_register_auth_configuration_response_from_dict = TableauAuthnV1RegisterAuthConfigurationResponse.from_dict(tableau_authn_v1_register_auth_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


