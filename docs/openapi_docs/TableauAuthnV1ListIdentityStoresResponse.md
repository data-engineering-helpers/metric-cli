# TableauAuthnV1ListIdentityStoresResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[TableauAuthnV1IdentityStoreInstance]**](TableauAuthnV1IdentityStoreInstance.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_list_identity_stores_response import TableauAuthnV1ListIdentityStoresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1ListIdentityStoresResponse from a JSON string
tableau_authn_v1_list_identity_stores_response_instance = TableauAuthnV1ListIdentityStoresResponse.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1ListIdentityStoresResponse.to_json())

# convert the object into a dict
tableau_authn_v1_list_identity_stores_response_dict = tableau_authn_v1_list_identity_stores_response_instance.to_dict()
# create an instance of TableauAuthnV1ListIdentityStoresResponse from a dict
tableau_authn_v1_list_identity_stores_response_from_dict = TableauAuthnV1ListIdentityStoresResponse.from_dict(tableau_authn_v1_list_identity_stores_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


