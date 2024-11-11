# TableauAuthnV1IdentityPool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_pool_id** | [**TableauAuthnV1UUID**](TableauAuthnV1UUID.md) |  | [optional] 
**identity_pool_name** | **str** | Identity pool name. Must be unique. This name is visible on the Tableau Server landing page when users sign in. | [optional] 
**identity_store_instance_id** | **int** | ID of the identity store instance configured with this identity pool. | [optional] 
**auth_type_instance_id** | **int** | ID of the authentication instance configured with this identity pool. | [optional] 
**is_enabled** | **bool** | The identity pool is enabled by default. | [optional] 
**created_at** | **str** | Date and time stamp of when the identity pool was configured. | [optional] 
**updated_at** | **str** | Date and time stamp of when the identity pool was updated. | [optional] 
**description** | **str** | Identity pool description displayed to users when they sign in. | [optional] 
**identity_store_type** | **str** | Identity store type used to provision users. | [optional] 
**auth_type** | **str** | Authentication type configured with this identity pool. | [optional] 

## Example

```python
from openapi_client.models.tableau_authn_v1_identity_pool import TableauAuthnV1IdentityPool

# TODO update the JSON string below
json = "{}"
# create an instance of TableauAuthnV1IdentityPool from a JSON string
tableau_authn_v1_identity_pool_instance = TableauAuthnV1IdentityPool.from_json(json)
# print the JSON string representation of the object
print(TableauAuthnV1IdentityPool.to_json())

# convert the object into a dict
tableau_authn_v1_identity_pool_dict = tableau_authn_v1_identity_pool_instance.to_dict()
# create an instance of TableauAuthnV1IdentityPool from a dict
tableau_authn_v1_identity_pool_from_dict = TableauAuthnV1IdentityPool.from_dict(tableau_authn_v1_identity_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


