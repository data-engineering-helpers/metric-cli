# TableauAuthnV1RegisterAuthConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Required. Authentication type. | [optional] 
**iframed_idp_enabled** | **bool** | Allows the identity provider (IdP) to authenticate inside of an iFrame. The IdP must disable clickjack protection to allow iFrame presentation. Default value is &#39;false&#39;. | [optional] 
**oidc** | [**TableauAuthnV1OidcConfig**](TableauAuthnV1OidcConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_register_auth_configuration_request import TableauAuthnV1RegisterAuthConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1RegisterAuthConfigurationRequest from a JSON string
tableau_authn_v1_register_auth_configuration_request_instance = TableauAuthnV1RegisterAuthConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1RegisterAuthConfigurationRequest.to_json())

# convert the object into a dict
tableau_authn_v1_register_auth_configuration_request_dict = tableau_authn_v1_register_auth_configuration_request_instance.to_dict()
# create an instance of TableauAuthnV1RegisterAuthConfigurationRequest from a dict
tableau_authn_v1_register_auth_configuration_request_from_dict = TableauAuthnV1RegisterAuthConfigurationRequest.from_dict(tableau_authn_v1_register_auth_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


