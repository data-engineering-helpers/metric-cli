# TableauAuthnV1ListIdentityPoolsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pools** | [**List[TableauAuthnV1IdentityPool]**](TableauAuthnV1IdentityPool.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_list_identity_pools_response import TableauAuthnV1ListIdentityPoolsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1ListIdentityPoolsResponse from a JSON string
tableau_authn_v1_list_identity_pools_response_instance = TableauAuthnV1ListIdentityPoolsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1ListIdentityPoolsResponse.to_json())

# convert the object into a dict
tableau_authn_v1_list_identity_pools_response_dict = tableau_authn_v1_list_identity_pools_response_instance.to_dict()
# create an instance of TableauAuthnV1ListIdentityPoolsResponse from a dict
tableau_authn_v1_list_identity_pools_response_from_dict = TableauAuthnV1ListIdentityPoolsResponse.from_dict(tableau_authn_v1_list_identity_pools_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


