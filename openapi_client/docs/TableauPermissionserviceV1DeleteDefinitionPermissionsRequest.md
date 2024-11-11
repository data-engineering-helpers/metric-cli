# TableauPermissionserviceV1DeleteDefinitionPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition_id** | **str** |  | [optional] 
**member_permissions** | [**List[TableauPermissionserviceV1MemberPermission]**](TableauPermissionserviceV1MemberPermission.md) |  | [optional] 

## Example

```python
from openapi_client.models.tableau_permissionservice_v1_delete_definition_permissions_request import TableauPermissionserviceV1DeleteDefinitionPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPermissionserviceV1DeleteDefinitionPermissionsRequest from a JSON string
tableau_permissionservice_v1_delete_definition_permissions_request_instance = TableauPermissionserviceV1DeleteDefinitionPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(TableauPermissionserviceV1DeleteDefinitionPermissionsRequest.to_json())

# convert the object into a dict
tableau_permissionservice_v1_delete_definition_permissions_request_dict = tableau_permissionservice_v1_delete_definition_permissions_request_instance.to_dict()
# create an instance of TableauPermissionserviceV1DeleteDefinitionPermissionsRequest from a dict
tableau_permissionservice_v1_delete_definition_permissions_request_from_dict = TableauPermissionserviceV1DeleteDefinitionPermissionsRequest.from_dict(tableau_permissionservice_v1_delete_definition_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


