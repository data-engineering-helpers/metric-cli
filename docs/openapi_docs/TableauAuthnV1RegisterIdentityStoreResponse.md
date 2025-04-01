# TableauAuthnV1RegisterIdentityStoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_instance** | [**TableauAuthnV1IdentityStoreInstance**](TableauAuthnV1IdentityStoreInstance.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_register_identity_store_response import TableauAuthnV1RegisterIdentityStoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1RegisterIdentityStoreResponse from a JSON string
tableau_authn_v1_register_identity_store_response_instance = TableauAuthnV1RegisterIdentityStoreResponse.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1RegisterIdentityStoreResponse.to_json())

# convert the object into a dict
tableau_authn_v1_register_identity_store_response_dict = tableau_authn_v1_register_identity_store_response_instance.to_dict()
# create an instance of TableauAuthnV1RegisterIdentityStoreResponse from a dict
tableau_authn_v1_register_identity_store_response_from_dict = TableauAuthnV1RegisterIdentityStoreResponse.from_dict(tableau_authn_v1_register_identity_store_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


