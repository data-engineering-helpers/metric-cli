# TableauAuthnV1UpdateAuthConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Required. Authentication instance ID. | [optional] 
**auth_type** | **str** | Required. Authentication type. | [optional] 
**iframed_idp_enabled** | **bool** | Allows the identity provider (IdP) to authenticate inside of an iFrame. The IdP must disable clickjack protection to allow iFrame presentation. Default value is &#39;false&#39;. | [optional] 
**oidc** | [**TableauAuthnV1OidcConfig**](TableauAuthnV1OidcConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_update_auth_configuration_request import TableauAuthnV1UpdateAuthConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1UpdateAuthConfigurationRequest from a JSON string
tableau_authn_v1_update_auth_configuration_request_instance = TableauAuthnV1UpdateAuthConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1UpdateAuthConfigurationRequest.to_json())

# convert the object into a dict
tableau_authn_v1_update_auth_configuration_request_dict = tableau_authn_v1_update_auth_configuration_request_instance.to_dict()
# create an instance of TableauAuthnV1UpdateAuthConfigurationRequest from a dict
tableau_authn_v1_update_auth_configuration_request_from_dict = TableauAuthnV1UpdateAuthConfigurationRequest.from_dict(tableau_authn_v1_update_auth_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


