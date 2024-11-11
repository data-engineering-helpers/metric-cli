# TableauAuthnV1RegisterIdentityStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Required. Identity store type used to provision users. Use 0 to configure a new local identity store. **Note:** Configuring a new identity store of type Active Directory or LDAP is not supported. | [optional] 
**name** | **str** | Required. Identity store name. Must be unique. | [optional] 
**display_name** | **str** | Identity store display name. | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_register_identity_store_request import TableauAuthnV1RegisterIdentityStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1RegisterIdentityStoreRequest from a JSON string
tableau_authn_v1_register_identity_store_request_instance = TableauAuthnV1RegisterIdentityStoreRequest.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1RegisterIdentityStoreRequest.to_json())

# convert the object into a dict
tableau_authn_v1_register_identity_store_request_dict = tableau_authn_v1_register_identity_store_request_instance.to_dict()
# create an instance of TableauAuthnV1RegisterIdentityStoreRequest from a dict
tableau_authn_v1_register_identity_store_request_from_dict = TableauAuthnV1RegisterIdentityStoreRequest.from_dict(tableau_authn_v1_register_identity_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


