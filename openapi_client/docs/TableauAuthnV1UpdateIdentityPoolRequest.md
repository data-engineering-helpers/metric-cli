# TableauAuthnV1UpdateIdentityPoolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Required. Identity pool ID. | [optional] 
**name** | **str** | Identity pool name. Must be unique. This name is visible on the Tableau Server landing page when users sign in. | [optional] 
**is_enabled** | **bool** | Identity pool is enabled by default. | [optional] 
**description** | **str** | Identity pool description displayed to users when they sign in. | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_update_identity_pool_request import TableauAuthnV1UpdateIdentityPoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1UpdateIdentityPoolRequest from a JSON string
tableau_authn_v1_update_identity_pool_request_instance = TableauAuthnV1UpdateIdentityPoolRequest.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1UpdateIdentityPoolRequest.to_json())

# convert the object into a dict
tableau_authn_v1_update_identity_pool_request_dict = tableau_authn_v1_update_identity_pool_request_instance.to_dict()
# create an instance of TableauAuthnV1UpdateIdentityPoolRequest from a dict
tableau_authn_v1_update_identity_pool_request_from_dict = TableauAuthnV1UpdateIdentityPoolRequest.from_dict(tableau_authn_v1_update_identity_pool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


