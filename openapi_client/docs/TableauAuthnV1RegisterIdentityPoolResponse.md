# TableauAuthnV1RegisterIdentityPoolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | [**TableauAuthnV1IdentityPool**](TableauAuthnV1IdentityPool.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_register_identity_pool_response import TableauAuthnV1RegisterIdentityPoolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1RegisterIdentityPoolResponse from a JSON string
tableau_authn_v1_register_identity_pool_response_instance = TableauAuthnV1RegisterIdentityPoolResponse.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1RegisterIdentityPoolResponse.to_json())

# convert the object into a dict
tableau_authn_v1_register_identity_pool_response_dict = tableau_authn_v1_register_identity_pool_response_instance.to_dict()
# create an instance of TableauAuthnV1RegisterIdentityPoolResponse from a dict
tableau_authn_v1_register_identity_pool_response_from_dict = TableauAuthnV1RegisterIdentityPoolResponse.from_dict(tableau_authn_v1_register_identity_pool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


