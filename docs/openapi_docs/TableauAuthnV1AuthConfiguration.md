# TableauAuthnV1AuthConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Authentication instance ID. | [optional] 
**created_at** | **str** | Date and time stamp of when the authentication instance was configured. | [optional] 
**updated_at** | **str** | Date and time stamp of when the authentication instance was updated. | [optional] 
**auth_type** | **str** |  | [optional] 
**iframed_idp_enabled** | **bool** | Allows the identity provider (IdP) to authenticate inside of an iFrame. The IdP must disable clickjack protection to allow iFrame presentation. Default value is &#39;false&#39;. | [optional] 
**oidc** | [**TableauAuthnV1OidcConfig**](TableauAuthnV1OidcConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_auth_configuration import TableauAuthnV1AuthConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1AuthConfiguration from a JSON string
tableau_authn_v1_auth_configuration_instance = TableauAuthnV1AuthConfiguration.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1AuthConfiguration.to_json())

# convert the object into a dict
tableau_authn_v1_auth_configuration_dict = tableau_authn_v1_auth_configuration_instance.to_dict()
# create an instance of TableauAuthnV1AuthConfiguration from a dict
tableau_authn_v1_auth_configuration_from_dict = TableauAuthnV1AuthConfiguration.from_dict(tableau_authn_v1_auth_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


