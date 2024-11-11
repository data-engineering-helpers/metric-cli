# TableauPermissionserviceV1HasEffectivePermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition_id** | **str** |  | [optional] 
**effective_permission_states** | [**List[TableauPermissionserviceV1PermissionState]**](TableauPermissionserviceV1PermissionState.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_permissionservice_v1_has_effective_permissions_response import TableauPermissionserviceV1HasEffectivePermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPermissionserviceV1HasEffectivePermissionsResponse from a JSON string
tableau_permissionservice_v1_has_effective_permissions_response_instance = TableauPermissionserviceV1HasEffectivePermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(TableauPermissionserviceV1HasEffectivePermissionsResponse.to_json())

# convert the object into a dict
tableau_permissionservice_v1_has_effective_permissions_response_dict = tableau_permissionservice_v1_has_effective_permissions_response_instance.to_dict()
# create an instance of TableauPermissionserviceV1HasEffectivePermissionsResponse from a dict
tableau_permissionservice_v1_has_effective_permissions_response_from_dict = TableauPermissionserviceV1HasEffectivePermissionsResponse.from_dict(tableau_permissionservice_v1_has_effective_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


