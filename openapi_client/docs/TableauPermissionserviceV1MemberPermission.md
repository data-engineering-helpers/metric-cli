# TableauPermissionserviceV1MemberPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** |  | [optional] 
**member_entity_type** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tableau_permissionservice_v1_member_permission import TableauPermissionserviceV1MemberPermission

# TODO update the JSON string below
json = "{}"
# create an instance of TableauPermissionserviceV1MemberPermission from a JSON string
tableau_permissionservice_v1_member_permission_instance = TableauPermissionserviceV1MemberPermission.from_json(json)
# print the JSON string representation of the object
print(TableauPermissionserviceV1MemberPermission.to_json())

# convert the object into a dict
tableau_permissionservice_v1_member_permission_dict = tableau_permissionservice_v1_member_permission_instance.to_dict()
# create an instance of TableauPermissionserviceV1MemberPermission from a dict
tableau_permissionservice_v1_member_permission_from_dict = TableauPermissionserviceV1MemberPermission.from_dict(tableau_permissionservice_v1_member_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


