# TableauPermissionserviceV1PermissionState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** |  | [optional] 
**has_permission** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_permissionservice_v1_permission_state import TableauPermissionserviceV1PermissionState

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPermissionserviceV1PermissionState from a JSON string
tableau_permissionservice_v1_permission_state_instance = TableauPermissionserviceV1PermissionState.from_json(json)
# print the JSON string representation of the object
print(TableauPermissionserviceV1PermissionState.to_json())

# convert the object into a dict
tableau_permissionservice_v1_permission_state_dict = tableau_permissionservice_v1_permission_state_instance.to_dict()
# create an instance of TableauPermissionserviceV1PermissionState from a dict
tableau_permissionservice_v1_permission_state_from_dict = TableauPermissionserviceV1PermissionState.from_dict(tableau_permissionservice_v1_permission_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


