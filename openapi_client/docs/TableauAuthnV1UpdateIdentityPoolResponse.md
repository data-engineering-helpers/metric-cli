# TableauAuthnV1UpdateIdentityPoolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | [**TableauAuthnV1IdentityPool**](TableauAuthnV1IdentityPool.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_update_identity_pool_response import TableauAuthnV1UpdateIdentityPoolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1UpdateIdentityPoolResponse from a JSON string
tableau_authn_v1_update_identity_pool_response_instance = TableauAuthnV1UpdateIdentityPoolResponse.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1UpdateIdentityPoolResponse.to_json())

# convert the object into a dict
tableau_authn_v1_update_identity_pool_response_dict = tableau_authn_v1_update_identity_pool_response_instance.to_dict()
# create an instance of TableauAuthnV1UpdateIdentityPoolResponse from a dict
tableau_authn_v1_update_identity_pool_response_from_dict = TableauAuthnV1UpdateIdentityPoolResponse.from_dict(tableau_authn_v1_update_identity_pool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


