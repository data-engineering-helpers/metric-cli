# TableauAuthnV1IdentityStoreInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identity store ID. | [optional] 
**type** | **str** | Identity store type used to provision users. | [optional] 
**name** | **str** | Identity store name. Must be unique. | [optional] 
**display_name** | **str** | Identity store display name. | [optional] 
**created_at** | **str** | Date and time stamp of when the identity store instance was created. | [optional] 
**updated_at** | **str** | Date and time stamp of when the identity store instance was updated. | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_identity_store_instance import TableauAuthnV1IdentityStoreInstance

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1IdentityStoreInstance from a JSON string
tableau_authn_v1_identity_store_instance_instance = TableauAuthnV1IdentityStoreInstance.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1IdentityStoreInstance.to_json())

# convert the object into a dict
tableau_authn_v1_identity_store_instance_dict = tableau_authn_v1_identity_store_instance_instance.to_dict()
# create an instance of TableauAuthnV1IdentityStoreInstance from a dict
tableau_authn_v1_identity_store_instance_from_dict = TableauAuthnV1IdentityStoreInstance.from_dict(tableau_authn_v1_identity_store_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


